# PipeChess 水井棋：房间与匹配系统说明

> 基于 `frontend/水井棋/PipeChess-master` 项目代码的总结，方便在 IDE 中查阅和参考。

---

## 1. 核心概念：`Game` = 一盘棋 + 一个房间

模型定义位置：`chess/models.py`，类 `Game`。

- **重要字段**
- `name`：房间名 / 房间号（字符串），例如 `"123456"` 或 `"ai123456"`。
- `board`：棋盘状态，`JSONField`，是一个二维数组。
- `player1` / `player2`：两个玩家，对应 Django 的 `User`。
- `winner`：赢家标记，`0=未结束，1 或 2 表示哪位玩家获胜`。
- `turn`：轮到哪一位玩家下，值为 `1` 或 `2`。
- `last_pipe`：最近画的一条线的位置，用于前端高亮。
- `create_time`：房间创建时间。

- **辅助属性示例**：

```python
@property
def is_ai(self):
    return self.name.lower().startswith('ai')

@property
def current_player(self):
    return getattr(self, 'player%d' % self.turn)

@property
def status(self):
    return {
        'board': self.board,
        'winner': self.winner,
        'turn': self.turn,
        'player1': self.player1.username if self.player1 else '',
        'player2': self.player2.username if self.player2 else '',
        'last_pipe': self.last_pipe,
    }
```

`status` 是前端轮询时获取的主要信息结构。

---

## 2. 游客随机昵称 + 自动登录

位置：`chess/views.py` 中的 `game` 视图和 `make_random_name`。

### 2.1 随机昵称生成

代码片段：

```python
VS = [... 一堆形容词 ...]
NS = [... 一堆名词 ...]


def make_random_name():
    v = random.choice(VS)
    n = random.choice(NS)
    name = v + '的' + n
    return name
```

效果：生成类似 `"豁达的孩子"`、`"漂亮的星星"` 这样的昵称。

### 2.2 未登录用户自动注册 + 登录

在 `views.game` 中：

```python
from django.contrib import auth
from models import Game

AI_NAME = 'Crazy AI'
PASSWORD = 'pipechess'


def game(request, name):
    ...
    user = request.user

    if not user.is_authenticated():
        username = make_random_name()
        user, created = User.objects.get_or_create(username=username)
        if created:
            user.set_password(PASSWORD)
            user.save()
        auth.login(request, user)
    ...
```

逻辑说明：

- 如果当前请求 **没有登录用户**：
  - 调用 `make_random_name()` 生成一个“形容词 + 名词”的昵称。
  - 在 `User` 表里 `get_or_create(username=昵称)`：
    - 如果是新用户，就设置一个统一默认密码 `PASSWORD` 并保存。
  - 调用 `auth.login(request, user)`，在浏览器里种登录 Cookie。
- 之后这个浏览器再次访问时就会被识别成同一个用户。

> 这种方式可以在任何网站里复用：给游客一个随机昵称，同时又使用 Django 的用户体系。

---

## 3. 创建房间：`/new/` 与 `?ai=1`

位置：`chess/views.py` 中的 `new` 视图。

```python
def new(request):
    ai = request.GET.get('ai', False)
    game_name = None
    for i in range(1000):
        game_name = str(random.randint(100000, 999999))
        if ai:
            game_name = 'ai' + game_name
        if not Game.objects.filter(name=game_name).exists():
            return HttpResponseRedirect('/game/%s/' % game_name)
    # clear games (理论上很少走到这里)
    t = timezone.now() - timezone.timedelta(hours=1)
    Game.objects.filter(last_pipe=[], create_time__lt=t)
    return HttpResponseRedirect('/game/1/')
```

流程说明：

- 从 100000–999999 随机生成 6 位数字作为房间号。
- 如果 URL 带有 `?ai=1`：
  - 在房间名前面加上 `"ai"` 前缀，例如 `"ai123456"`，表示 AI 对局房间。
- 检查数据库里是否已经存在同名房间：
  - 若不存在，直接 **重定向** 到 `/game/<房间名>/`。
  - 真正的 `Game` 记录由 `game()` 视图里的 `get_or_create` 负责创建。

> 这样 `/new/` 就是“创建房间”的入口，`/new/?ai=1` 是“创建 AI 对局房间”的入口。

---

## 4. 匹配对局：`/match/`

位置：`chess/views.py`，函数 `match`。

```python
def match(request):
    user = request.user
    t = timezone.now() - timezone.timedelta(minutes=5)
    game = Game.objects.filter(
        player2__isnull=True,
        create_time__gt=t
    ).exclude(player1=user).order_by('-create_time').first()
    if game:
        return HttpResponseRedirect('/game/%s/' % game.name)
    return HttpResponseRedirect('/new/')
```

逻辑说明：

- 只在 **最近 5 分钟** 内创建的房间中查找：`create_time__gt=t`。
- 条件：
  - `player2__isnull=True`：说明房间里只有一个人，还差一个玩家。
  - `exclude(player1=user)`：避免匹配到自己创建、自己等待的房间。
- 找到最新的这样的房间就：
  - 重定向 `/game/<该房间号>/`，当前用户作为 `player2` 加入。
- 如果找不到符合条件的房间：
  - 重定向到 `/new/`，新建一个房间等待别人加入。

> 这就是一个简单易懂的匹配机制：
> - 有合适的“半满房间”就加入；
> - 否则就自己新建一个房间。

---

## 5. 进入房间 + 分配玩家 1 / 玩家 2

位置：`chess/views.py` 的 `game` 视图。

```python
def game(request, name):
    request.session['game_name'] = name
    request.session.save()

    user = request.user
    # 1. 游客自动生成昵称 + 登录（见上文）

    game, created = Game.objects.get_or_create(name=name)

    # 2. AI 房间：如果没人，就先放 AI 进去
    if game.is_ai and not game.player1 and not game.player2:
        ai, created = User.objects.get_or_create(username=AI_NAME)
        if random.random() > 0.5:
            game.player1 = ai
        else:
            game.player2 = ai
        game.save()

    # 3. 分配玩家位置
    if not game.player1:
        game.player1 = user
        game.save()
    elif not game.player2 and game.player1 != user:
        game.player2 = user
        game.save()

    return render_to_response('game.html', locals())
```

分配规则总结：

- **记录最近访问的房间号**：`request.session['game_name'] = name`。
- **AI 房间特殊逻辑**：
  - 若 `name` 以 `ai` 开头、且房间当前两个位置都为空：
    - 创建/获取 `Crazy AI` 用户。
    - 随机把 AI 放到 `player1` 或 `player2`。
- **普通玩家分配**：
  - 如果 `player1` 为空 → 当前用户 = `player1`。
  - 否则，如果 `player2` 为空且 `player1 != 当前用户` → 当前用户 = `player2`。
  - 如果两个位置都满了，则当前用户相当于是“围观者”。

---

## 6. 实际“找朋友一起玩”的用法

从用户视角看，这套设计支持多种场景：

- **创建房间 + 分享房间号/链接**
- 打开 `/new/`（或前端“创建房间”按钮）。
- 浏览器地址会变成 `/game/123456/` 这样的 URL。
- 把 `123456` 或整条 URL 发给朋友。
- 朋友在自己的浏览器中打开 `/game/123456/`：
  - 会自动变成 `player2`，直接对弈。

- **快速匹配对局**
- 两个玩家都访问 `/match/`：
  - 第一个玩家：如果暂时没人，就新建一个房间等待。
  - 第二个玩家：自动匹配进入第一个玩家的房间。

- **房间号加入（页面上的“进入指定房间”）**
- 前端在 `game.html` 中使用：

  ```javascript
  $('#join').click(function () {
      bootbox.prompt({
          title: '输入房间编号',
          value: '{{ game.name }}',
          callback: function (name) {
              if(name){
                  top.location = '/game/' + name + '/';
              }
          }
      });
  });
  ```

- 用户在弹窗中输入房间号，即跳转到 `/game/<房间号>/`，实现“手动加入指定房间”。

---

## 7. 如何在你自己的项目中复用这套思路

无论你后端是 Django / Flask / FastAPI，整体思路都可以参考：

- **游客昵称系统**
- 定义两组词表（形容词列表 + 名词列表），随机组合生成昵称。
- 未登录请求访问房间或匹配接口时：
  - 在用户表中以昵称 `get_or_create` 一个用户。
  - 自动登录（或在你的系统中保存 session / token）。

- **房间模型**
- 最少包含：
  - `room_id` / `name`、`player1_id`、`player2_id`、`status`（棋盘或其它游戏状态）、`create_time`。

- **创建房间接口** `/new`
- 生成一个不会重复的房间号，重定向/返回该房间链接。

- **匹配接口** `/match`
- 查找“只差一个玩家”的房间（例如 `player2` 为空且在一定时间内创建）。
- 如果找到，就返回/重定向到该房间；否则新建一个。

- **进入房间接口** `/room/<id>` 或 `/game/<id>`
- 根据当前登录用户为房间分配 `player1` 或 `player2` 角色。
- 已满则视为围观者，只能看不能操作。

这就是 PipeChess 房间系统与随机昵称登录的完整思路，已经整理在本文件中，方便你随时参考或在自己的项目里实现类似功能。

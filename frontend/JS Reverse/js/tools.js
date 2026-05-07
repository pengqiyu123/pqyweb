(function (global) {
  function wireTools() {
    bindClick('jsr-tool-base64-encode', function () {
      setValue('jsr-tool-base64-output', btoa(getValue('jsr-tool-base64-input')));
    });
    bindClick('jsr-tool-base64-decode', function () {
      try {
        setValue('jsr-tool-base64-output', atob(getValue('jsr-tool-base64-input')));
      } catch (error) {
        setValue('jsr-tool-base64-output', 'Base64 解码失败');
      }
    });

    bindClick('jsr-tool-md5', function () {
      setValue('jsr-tool-hash-output', global.CryptoJS.MD5(getValue('jsr-tool-hash-input')).toString());
    });
    bindClick('jsr-tool-sha256', function () {
      setValue('jsr-tool-hash-output', global.CryptoJS.SHA256(getValue('jsr-tool-hash-input')).toString());
    });

    bindClick('jsr-tool-aes-encrypt', function () {
      var key = getValue('jsr-tool-aes-key');
      var text = getValue('jsr-tool-aes-input');
      setValue('jsr-tool-aes-output', global.CryptoJS.AES.encrypt(text, key).toString());
    });
    bindClick('jsr-tool-aes-decrypt', function () {
      try {
        var key = getValue('jsr-tool-aes-key');
        var text = getValue('jsr-tool-aes-input');
        var decrypted = global.CryptoJS.AES.decrypt(text, key).toString(global.CryptoJS.enc.Utf8);
        setValue('jsr-tool-aes-output', decrypted || 'AES 解密失败');
      } catch (error) {
        setValue('jsr-tool-aes-output', 'AES 解密失败');
      }
    });

    bindClick('jsr-tool-beautify', function () {
      var beautify = typeof global.js_beautify === 'function'
        ? global.js_beautify
        : (global.beautifier && typeof global.beautifier.js === 'function' ? global.beautifier.js : null);
      if (!beautify) {
        setValue('jsr-tool-beautify-output', '格式化器未加载');
        return;
      }
      setValue('jsr-tool-beautify-output', beautify(getValue('jsr-tool-beautify-input')));
    });

    bindClick('jsr-tool-to-hex', function () {
      var input = getValue('jsr-tool-hex-input');
      var result = '';
      for (var i = 0; i < input.length; i += 1) {
        result += input.charCodeAt(i).toString(16).padStart(2, '0');
      }
      setValue('jsr-tool-hex-output', result);
    });

    bindClick('jsr-tool-from-hex', function () {
      try {
        var hex = getValue('jsr-tool-hex-input').replace(/\s+/g, '');
        var output = '';
        for (var i = 0; i < hex.length; i += 2) {
          output += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
        }
        setValue('jsr-tool-hex-output', output);
      } catch (error) {
        setValue('jsr-tool-hex-output', 'Hex 转换失败');
      }
    });
  }

  function bindClick(id, handler) {
    var node = document.getElementById(id);
    if (node) {
      node.addEventListener('click', handler);
    }
  }

  function getValue(id) {
    var node = document.getElementById(id);
    return node ? node.value : '';
  }

  function setValue(id, value) {
    var node = document.getElementById(id);
    if (node) {
      node.value = value;
    }
  }

  global.JSReverseTools = {
    wire: wireTools
  };
})(window);

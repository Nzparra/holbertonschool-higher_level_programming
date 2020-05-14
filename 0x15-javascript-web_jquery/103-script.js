const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    hello();
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      hello();
    }
  });
};

function hello () {
  const lang = $('INPUT#language_code').val();
  $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lang, function (data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
}

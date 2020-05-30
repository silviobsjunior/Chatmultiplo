!function(){"use strict"; 
  alert("A URL desta pagina é: " + window.location.href);
      
  var pathArray = window.location.href;

  var pathArray = pathArray.split( '/' );

  var sellerer = pathArray[3];

  if (sellerer === 'shopinconfidentes') {
    window.open('https://www.instagram.com/shopinconfidentes/?hl=pt-br');
  } else if (sellerer === 'teste') {
    window.open('https://www.instagram.com/benzadeusloja/?hl=pt-br');
  } else if (sellerer === 'duopassos') {
    window.open('https://www.instagram.com/sapatilhasduopassos/?hl=pt-br');
  } else {
    window.open('https://pt.khanacademy.org/login');
  }
}
            };

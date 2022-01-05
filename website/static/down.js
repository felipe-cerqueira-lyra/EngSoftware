function copy_link(){
  var link = document.getElementById('Link');
  navigator.clipboard.writeText(link.textContent);
  console.log(link.textContent)
}

console.log('Hello World!')

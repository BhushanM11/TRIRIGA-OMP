document.getElementById("ompForm").addEventListener("submit", function(event){
  event.preventDefault();
  
  // let uname = document.getElementById("uname").value;
  // let pname = document.getElementById("pname").value;
  // let pass  = document.getElementById("pass").value;
  // let url   = document.getElementById("url").value;

  var formData = new FormData(this);

  fetch('/create_qr', {method: "POST", body: formData})
    .then(response => response.json())
  
  // fetch('http://localhost:5000/create-package', {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type': 'application/json',
  //   },
  //   body: JSON.stringify({username: uname, packageName: pname, password: pass, environment: url}),
  // })
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
});
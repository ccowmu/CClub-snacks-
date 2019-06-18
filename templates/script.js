checkout=document.getElementById("checkout");
function row(name,cost){
   var newRow=checkout.insertRow(1);
   var cell1=newRow.insertCell(0);
   var cell2=newRow.insertCell(1);
   var cell3=newRow.insertCell(2);
   var cell4=newRow.insertCell(3);
   cell1.innerHTML=name;
   cell2.innerHTML=cost;
   cell3.innerHTML="1";
   cell4.innerHTML=cost;  
   }  

function remove()  {
   var remove=checkout.rows.length();
   for(var i=  1; i<remove;  i++)    {
      document.getElementById("checkout").deleteRow(1);
      }
   }

function cancelMessage() {
   remove();
   document.getElementById('message').innerHTML='you canceled your order.';
   }

function chargeMessage(){
   remove();
   document.getElementById("message").innerHTML="thankyou for your order";
   }
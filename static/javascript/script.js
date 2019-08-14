// row function which defines the rows and the initial data.
 function insert(name,cost){
      checkout=document.getElementById('checkout');
      //Warning!!! This next block does not currently work
      //isolate table rows
      comparer= document.getElementsByTagName('tr');
      //boolean for checking whether or not the snack is already in the table
      checker = false;
      var rowcount = checkout.rows.length;
      var iRow;
      //for loop that iterates across the table to see if name is in there
      for(var i = 0; i < rowcount; i++)   {
          if(comparer[i].getAttribute("id") == name) {
            checker = true;
            iRow = comparer[i];
          }
      }
      if(checker == true) {
        iCells = iRow.cells;
        iCells[2].innerHTML = parseInt(iCells[2].innerHTML) + 1;
        iCells[3].innerHTML = parseFloat(iCells[3].innerHTML) + cost;
      }
      else {
      // inserts a new row at index 1
      iRow = checkout.insertRow(1)

// defines the cells for our row
      var cell1=iRow.insertCell(0);
      var cell2=iRow.insertCell(1);
      var cell3=iRow.insertCell(2);
      var cell4=iRow.insertCell(3);

// inserts the appropriate content in the rows
      iRow.id=name;
      iRow.class= "table_row";
      cell1.innerHTML=name;
      cell2.innerHTML=cost;
      cell3.innerHTML="1";
      cell4.innerHTML=cost;
    }
    }
// added a remove function which will remove the rows from the table
  function remove()  {
      checkout=document.getElementById("checkout");
      var rowCount=checkout.rows.length;
      for(var i =  1; i < rowCount;  i++)    {
        document.getElementById("checkout").deleteRow(1);
       }
    }

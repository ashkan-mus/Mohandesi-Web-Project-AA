$('.plus-card').click(function(){
    var id=$(this).attr("pid").toString();
    console.log("pid =", id)
    $.ajax({
        type:"GET",
        url:"/pluscard",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data =", data);
            Element.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount

        }
    })

})


$('.remove-card').click(function(){
    var id=$(this).attr("pid").toString();
    var Element=this
    $.ajax({
        type:"GET",
        url:"/removecard",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data =", data);
            Element.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
            Element.parentNode.parentNode.parentNode.parentNode.remove()

        }
    })
    
})
function details()
{
    tok = window.localStorage.getItem('token');
    $.ajax({
        type:"GET",
        url:"https://127.0.0.1:8000/access",

        headers:
        {
            "Authorization": 'Bearer ' + tok
        },

        success: function(res)
        {
            console.log(res)
            authorized(res)
        },
        error:function(error)
        {
            console.log(error)
            unauthorized()
        }
    })
}

function authorized(data)
{
    var p1 = document.createElement('p')
    var p2 = document.createElement('p')
    p1.appendChild(document.createTextNode('Email: ' + data.email))
    p2.appendChild(document.createTextNode('Username: ' + data.username))
    document.body.appendChild(p1)
    document.body.appendChild(p2)
}
function unauthorized()
{
    var h2 = document.createElement('h2')
    h2.appendChild(document.createTextNode('You are Not authorized'))
    document.body.appendChild(h2)
}

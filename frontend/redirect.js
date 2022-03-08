function send_code()
{
    const params = new Proxy(new URLSearchParams(window.location.search), {
        get: (searchParams, prop) => searchParams.get(prop),
      });
      // Get the value of "some_key" in eg "https://example.com/?some_key=some_value"
      let value = params.code; // "some_value"
      provider = window.localStorage.getItem('provider');
    $.ajax({ 
                type : 'GET',
                url : "https://127.0.0.1:8000/redirect/" + provider,
                data:
                {
                    'code':value
                },
                success: function(res){
                h1(res.User.email)
                h2(res.User.provider)
                console.log(res)
            },
            error: function(error) {
                console.log(error)
            }
            })
}

function h1(text) {
    var h1 = document.createElement('h1');
    h1.appendChild(document.createTextNode(text));
    document.body.appendChild(h1);
}
function h2(text) {
    var h2 = document.createElement('h2');
    h2.appendChild(document.createTextNode(text));
    document.body.appendChild(h2);
}
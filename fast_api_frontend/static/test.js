function httpGetDiscord() 
{
    window.location = "https://discord.com/api/oauth2/authorize?client_id=" + DISCORD_CLIENT_ID + "&redirect_uri=http%3A%2F%2F127.0.0.1%3A5500%2Ffrontend%2Fredirect.html&response_type=code&scope=email"
    window.localStorage.setItem('provider', 'discord');
}
function httpGetGoogle()
{
    window.location = "https://accounts.google.com/o/oauth2/v2/auth?client_id=" + GOOGLE_CLIENT_ID + "&redirect_uri=http://127.0.0.1:5500/frontend/redirect.html&access_type=offline&response_type=code&scope=https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
    window.localStorage.setItem('provider', 'google');
}
function httpGetLinkedIn()
{
    window.location = "https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=" + LINKEDIN_CLIENT_ID + "&redirect_uri=http://127.0.0.1:5500/frontend/redirect.html&state=foobar&scope=r_liteprofile r_emailaddress"
    window.localStorage.setItem('provider', 'linkedin');
}

function httpGetFacebook()
{
    window.location = "https://www.facebook.com/v12.0/dialog/oauth?client_id=463196508605331&redirect_uri=http://localhost:5500/frontend/redirect.html&state=blank&scope=email";
    window.localStorage.setItem('provider', 'facebook');

}
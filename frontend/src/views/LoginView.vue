<template>
    <Navbar />
    <div class="login-view">
        <div class="login-form-container">
            <h1 class="login-title">Log In</h1>
            <form class="login-form">
                <input type="text" placeholder="Username">
                <input type="password" placeholder="Password">
                <button type="submit">Log In</button>
                <router-link class="register-link" to="/register">Don't have an account? Sign up here!</router-link>
            </form>
        </div>
    </div>
</template>

<script>
import Navbar from '@/components/PickleNavbar.vue'


 export default {
     name: 'LoginView',
     components: {
         Navbar
     }
 }
</script>

<style>
.login-view{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: start;
    height: 90vh;
    background-color: var(--darkpink);
}

.login-form-container{
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    border: none;
}

.login-form{
    display: flex;
    flex-direction: column;
    align-items: center;
}

.login-form input[type="text"],
.login-form input[type="password"] {
    padding: 10px;
    margin: 10px;
    border-radius: 10px;
    border: 1px solid #ccc;
    width: 90%;
}

.login-form button {
    background-color: var(--pink);
    color: white;
    border: none;
    padding: 10px 20px;
    text-align: center;
    font-size: 1em;
    margin: 10px;
    border-radius: 10px;
}
.login-form button:hover {
    background-color: var(--lightpink);
}

.register-link{
    color: white;
    margin-top: 10px;
}



</style>
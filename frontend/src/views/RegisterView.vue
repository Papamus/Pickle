<template>
    <Navbar />
    <div class="register-view">
        <div class="register-form-container">
            <h1 class="register-title">Register</h1>
            <form class="register-form">
                <input type="text" placeholder="Username" required>
                <input type="email" placeholder="Email" required>
                <input type="password" placeholder="Password" required>
                <input type="password" placeholder="Confirm Password" required>
                <div class="additional-info">
                    <input type="checkbox" id="terms" required>
                    <label for="terms">I agree to the Terms of Service and Privacy Policy</label>
                </div>
                <button type="submit">Register</button>
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
.register-view{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: start;
    height: 90vh;
    background-color: var(--darkpink);
}

.register-form-container{
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    border: none;
}

.register-form{
    display: flex;
    flex-direction: column;
    align-items: center;
}

.register-form input[type="text"],
.register-form input[type="email"],
.register-form input[type="password"] {
    padding: 10px;
    margin: 10px;
    border-radius: 10px;
    border: 1px solid #ccc;
    width: 90%;
}

.additional-info{
    margin: 10px;
}

#terms{
    margin-right: 10px;
}

.register-form button {
    background-color: var(--pink);
    color: white;
    border: none;
    padding: 10px 20px;
    text-align: center;
    font-size: 1em;
    margin: 10px;
    border-radius: 10px;
}

.register-form button:hover {
    background-color: var(--lightpink);
}

</style>
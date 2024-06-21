<template>
  <div id="app">
    <HomeView />
  </div>
</template>

<script>
import HomeView from './views/HomeView.vue'

export default {
  name: 'App',
  components: {
    HomeView
  }
}
</script>

<style>
body {
  font-family: Arial, Helvetica, sans-serif;
  background-color: var(--darkpink);
  
  --darkpink: #FF0A54;
  --lightpink: #FF8DAB;
  --pink: #FF487F;
  --lightpurple: #C77CF9;
  --darkpurple: #B450F7;
}

/* fonts */
h1 {
  font-size: 3em;
  color: white;
}
h2 {
  font-size: 2em;
  color: white;
}
h3 {
  font-size: 1.5em;
  color: white;
}
p {
  font-size: 1em;
  font-weight: 100;
  color: white;
}


/* buttons */
.default-button {
  background-color: var(--pink);
  color: white;
  border: none;
  padding-left: 30px;
  padding-right: 30px;
  padding-top: 10px;
  padding-bottom: 10px;
  text-align: center;
  font-size: 0.7em;
  margin-right: 20px;
  margin-left: 20px;
  border-radius: 10px;
  cursor: pointer;
}
.default-button:hover {
  background-color: var(--lightpink);
}
.default-button:active {
  background-color: var(--lightpink);
  font-weight: 400;
}

/* forms */
.modal{
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: opacity 0.3s ease;
}

.modal-content{
  background-color: var(--lightpink);
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 90%;
  max-width: 550px;
}

.close{
  float: right;
  font-size: 28px;
  cursor: pointer;
}

input[type="text"],
input[type="number"] {
  padding: 10px;
  margin: 10px;
  border-radius: 10px;
  border: 1px solid #ccc;
  width: 90%;
}

.modal-button {
  background-color: var(--pink);
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  font-size: 1em;
  margin: 10px;
  border-radius: 10px;
}
.modal-button:hover {
  background-color: var(--darkpink);
}
.modal-h2 {
  text-align: center;
}

</style>

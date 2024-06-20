<template>
    <div>
      <Navbar />
      
      <div class="main-container">
  
        <div class="left-container">
          <!-- left section - timer and approx time left-->
          <div class="timer">
              <div class="controls">
                <button @click="setActivity('work')">Pickle</button>
                <button @click="setActivity('shortBreak')">Short break</button>
                <button @click="setActivity('longBreak')">Long break</button>
              </div>
              <h1>{{ time }}</h1>
              <div class="time">{{ formattedTime }}</div>
              <button v-if="!isRunning" @click="startTimer">Start</button>
              <button v-else @click="stopTimer">Stop</button>
              <button @click="nextActivity">Skip</button>
          </div>
  
          <!-- approx time and tasks left -->
          <div class="approx-time-left">
            <p>Pickles: {{ completedPicklesCount }}/{{ totalPicklesCount }}</p>
            <p>Finish At: {{ estimatedTimeLeft }}</p>
            
          </div>
        </div>
  
  
  
        <div class="right-container">
         <!-- right section - tasks list and add task btn -->
          <div class="task-list">
              <h1>Your tasks</h1>
              <ul>
                <li v-for="(task,index) in activeTasks" :key="index">
                  <div class="task-item">
                    <div class="task-title">{{ task.title }}</div>
                    <div class="task-description" v-if="task.description">{{ task.description }}</div>
                    <div class="task-pickles">{{ task.pickles }} </div>
                    <button @click="markTaskAsCompleted(index)">Mark as completed</button>
                  </div>
                </li>
              </ul>
              <p v-if="tasks.length === 0">Seems like there are no tasks left...</p>
              <h1>Completed tasks</h1>
              <ul>
                <li v-for="(task,index) in completedTasks" :key="index">
                  <div class="task-item">
                    <div class="task-title">{{ task.title }}</div>
                    <div class="task-description" v-if="task.description">{{ task.description }}</div>
                    <div class="task-pickles">{{ task.pickles }}</div>
                  </div>
                </li>
              </ul>
  
          </div>
  
  
          <div class="add-task">
            <button @click="showAddTaskPopup">Add task</button>
          </div>
        </div>
  
  
  
        <div class="modal" v-if="showPopup">
          <div class="modal-content">
            <span class="close" @click="showPopup = false">&times;</span>
            <h2>Add a task</h2>
            <input type="text" v-model="newTask.title" placeholder="Title">
            <input type="text" v-model="newTask.description" placeholder="Description">
            <input type="number" v-model="newTask.pickles" placeholder="Pickles">
            <button @click="addTask">Add</button>
          </div>
        </div>
  
      </div>
      
    </div>
  </template>
  
  <script>
    import Navbar from '../components/PickleNavbar.vue';
  
  
  
    export default {
      components: {
        Navbar
      },
      data() {
        return {
          minutes: 25,
          seconds: 0,
          timer: null,
          isRunning: false,
          activity: 'work', // 'work', 'shortBreak', 'longBreak',
          tasks: [],
          newTask: {
           title: '',
           description: '',
           pickles: null,
           completed: false,
          },
          showPopup: false,
        };
      },
      computed: {
        formattedTime() {
          const minutes = this.minutes < 10 ? `0${this.minutes}` : this.minutes;
          const seconds = this.seconds < 10 ? `0${this.seconds}` : this.seconds;
          return `${minutes}:${seconds}`;
        },
        totalPicklesCount() {
          return this.tasks.reduce((total, task) => total + task.pickles, 0);
        },
        completedPicklesCount() {
          return this.tasks.reduce((total, task) => task.completed ? total + task.pickles : total, 0);
        },
        estimatedTimeLeft() {
          const now = new Date();
          const totalPicklesMinutes = this.totalPicklesCount * 25;
          const finishTime = new Date(now.getTime() + totalPicklesMinutes * 60 * 1000);
  
          return `${finishTime.getHours()}:${finishTime.getMinutes()}`;
        },
        completedTasks(){
          return this.tasks.filter(task => task.completed);
        },
        activeTasks(){
          return this.tasks.filter(task => !task.completed);
        },
      },
      methods: {
        startTimer() {
          if (this.timer) {
            clearInterval(this.timer);
          }
          this.isRunning = true;
          this.timer = setInterval(() => {
            if (this.seconds === 0) {
              if (this.minutes === 0) {
               this.nextActivity();
              } else {
                this.minutes -= 1;
                this.seconds = 59;
              }
            } else {
              this.seconds -= 1;
            }
          }, 1000);
        },
        stopTimer() {
          clearInterval(this.timer);
          this.isRunning = false;
        },
        setActivity(activity) {
          clearInterval(this.timer);
          this.isRunning = false;
          this.activity = activity;
          switch (activity) {
            case 'work':
              this.minutes = 25;
              this.seconds = 0;
              break;
            case 'shortBreak':
              this.minutes = 5;
              this.seconds = 0;
              break;
            case 'longBreak':
              this.minutes = 15;
              this.seconds = 0;
              break;
          }
        },
        nextActivity() {
          clearInterval(this.timer);
          this.isRunning = false;
          if (this.activity === 'work'){
            this.activity = 'shortBreak';
            this.minutes = 5;
          }
          else if (this.activity == 'shortBreak' || this.activity == 'longBreak'){
            this.activity = 'work';
            this.minutes = 25;
          }
          this.seconds = 0;
        },
        showAddTaskPopup() {
          this.showPopup = true;
        },
        closePopup() {
          this.showPopup = false;
          this.clearNewTask();
        },
        clearNewTask() {
          this.newTask = {
            title: '',
            description: '',
            pickles: null,
            completed: false,
          };
        },
        addTask() {
          if (this.newTask.title !== "" && this.newTask.pickles !== null && this.newTask.pickles > 0) {
            this.tasks.push({
              title: this.newTask.title,
              description: this.newTask.description,
              pickles: this.newTask.pickles,
              completed: false,
            });
            this.closePopup();
          }
          else {
            alert('Please fill in the title and pickles correctly!');
            this.clearNewTask();
          }
        },
        markTaskAsCompleted(index) {
          this.tasks[index].completed = true;
        },
  
  
        login() {
          // Placeholder for login
        }
      }
    }
  </script>
  
  <style scoped>
    .navbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 20px;
      background-color: #f8f9fa;
      border-bottom: 1px solid #e9ecef;
    }
    .navbar-left {
      display: flex;
      align-items: center;
    }
    .navbar-right {
      display: flex;
      align-items: center;
    }
    .navbar-app-name {
      font-size: 1.5em;
    }
    .navbar-button {
      margin-left: 10px;
      padding: 5px 10px;
      border: 1px solid;
      border-radius: 10%;
      background-color: #007bff;
      color: white;
    }
  
    .main-container {
      display: flex;
      justify-content: space-between;
      margin: 20px;
      align-items: flex-start;
      width: 90%;
    }
    .left-container {
      width: 65%;
    }
    .right-container {
      width: 35%;
    }
  
  
  
  
    .timer {
      font-size: 2em;
      text-align: center;
    }
    .time {
      font-size: 1.5em;
      margin: 20px 0;
    }
  
    button {
      padding: 10px 20px;
      margin: 10px;
      font-size: 1em;
      border: 1px solid;
      border-radius: 10%;
      background-color: #007bff;
      color: white;
    }
  
  
    .task-list {
      font-size: 1.5em;
    }
    .task-list ul {
      list-style-type: none;
      padding: 0;
    }
    .task-item {
      margin: 10px 0;
      border: 1px solid #e9ecef;
    }
    .add-task {
      margin-top: 20px;
      text-align: center;
    }
    .add-task button {
      padding: 10px 20px;
      font-size: 1em;
      border: 1px solid;
      border-radius: 10%;
      background-color: #007bff;
      color: white;
    }
    .modal{
      display: block;
      position: fixed;
      z-index: 1;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      overflow: auto;
      background-color: rgba(0, 0, 0, 0.4);
    }
  </style>
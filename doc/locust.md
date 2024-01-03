**Users:**

This refers to the number of simulated users that will be making requests against your system.
Each "user" is essentially a separate thread or process that performs actions (like sending HTTP requests, interacting with a website, etc.) as defined in your Locust test script.
When you set the number of users, you are deciding how many of these concurrent users will be simulating the load on your system. For example, setting it to 100 means 100 users will be simultaneously interacting with your system.

**Spawn Rate:**

This defines how quickly Locust will spawn these users.
It's the rate at which new users are added to the test until the total number of specified users is reached.
For instance, if you set the spawn rate to 10 and the total number of users to 100, Locust will start 10 new users every second until it reaches 100 total users.
The spawn rate helps in gradually increasing the load on the system, rather than starting all users at once, which can be more realistic and less shocking to the system under test.
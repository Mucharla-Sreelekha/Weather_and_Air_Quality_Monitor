**Weather and Air Quality Monitoring Application**

**Project Overview**

The **Weather and Air Quality Monitoring Application** is a comprehensive platform that combines real-time weather and air quality monitoring with features for user interaction and community engagement. This project was designed to provide valuable environmental insights while fostering a collaborative community.

Features

1. **User Authentication**
    - Registration: Users can sign up with secure password handling.
    - Login: Existing users can log in to access their dashboard.

2. **Weather and Air Quality Dashboard**
    - Real-time weather updates and Air Quality Index (AQI) data.
    - Displays weather trends and air quality visualizations using Chart.js.

3. **Carbon Tracking**
    - Track and manage your carbon footprint.
    - Personalized recommendations to reduce environmental impact.

4. **Community Platform**
    - Users can share posts related to environmental issues, solutions, or any topic of interest.
    - Features include:
    - **Admin Controls**: 
        - Approve or delete user posts.
        - Send email notifications to users regarding post approval or deletion.
    - **User Interactions**:
        - Like or comment on posts.
        - Email notifications sent to the post author when their post receives a like or comment.

5. **Email Notifications**
   - Automated email notifications for:
       - Post approval or deletion by the admin.
       - User interactions (likes or comments) on posts.

Technology Stack
  - **Frontend**: HTML, CSS, Bootstrap
  - **Backend**: Python, Flask
  - **Database**: MySQL
  - **Visualization**: Chart.js
  - **Email Notifications**: Flask-Mail

Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Mucharla-Sreelekha/Weather_and_Air_Quality_Monitor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Weather_and_Air_Quality_Monitor
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   - Create a MySQL database.
   - Import the provided SQL schema to set up the necessary tables.
   - Update the database credentials in the Flask application.
5. Run the application:
   ```bash
   flask run
   ```
6. Access the application at `http://127.0.0.1:5000/`.

## Usage
1. Register an account or log in if you already have an account.
2. Explore the Weather and Air Quality Dashboard.
3. Track your carbon footprint.
4. Engage with the community by creating posts, liking, and commenting.
5. Admins can manage posts via the admin panel.

*Screenshots*

**Weather & Environment Dashboard**
![Weather Dashboard](https://github.com/user-attachments/assets/b5226369-bd90-481e-9bf8-318eeb293787)


**Latest News Articles**
![Latest News](https://github.com/user-attachments/assets/a897b0dd-ff56-48bb-8b9a-1180c1d850c5)


**Charts**
![Charts](https://github.com/user-attachments/assets/0361d6a2-f0e4-4248-ad39-f50bc0781df5)

**Login Page**
![Login Page](https://github.com/user-attachments/assets/c96fb4b2-e893-4b14-8766-75c0333a11c6)


**Register Page**
![Register Page](https://github.com/user-attachments/assets/8447d945-87c6-4a51-9e00-07112670306a)


**Carbon Tracking Interface**
![Carbon Tracking](https://github.com/user-attachments/assets/639dcc26-1c6f-473e-9643-5ab0d80d2613)


**Leader Board**
![Leaderboard](https://github.com/user-attachments/assets/7ab3e48b-3f09-4680-bf54-126263f8c13e)


**Community Platform**
![Community Platform](https://github.com/user-attachments/assets/78cb5289-c7be-4ddb-83fb-ec4d4b0174d0)



Future Enhancements
- Integration of predictive analytics for weather and AQI trends.
- Enhanced user profiles with more customization options.
- Mobile application support.

Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

License
This project is licensed under the **MIT License**.

Acknowledgments
- **Infosys Springboard 5.0**: Inspiration and guidance for project development.
- OpenWeatherMap: Weather and AQI data API.

---
Feel free to connect and contribute to make this application even better!

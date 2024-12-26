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
![Weather Dashboard](https://github.com/user-attachments/assets/c22716b5-4a56-4a0d-a132-5776d0ac11a1)

**Latest News Articles**
![Latest News](https://github.com/user-attachments/assets/574436b4-2985-4c98-ac27-549edfb7835b)

**Charts**
![Charts](https://github.com/user-attachments/assets/f8a6728a-3e34-4640-bbfd-fe8c7afd7290)

**Login Page**
![Login Page](https://github.com/user-attachments/assets/39b8d301-8a87-4ffc-9eff-13cffcec174d)

**Register Page**
![Register Page](https://github.com/user-attachments/assets/59bd7e82-1c2d-4128-83e2-1a099ca88856)

**Carbon Tracking Interface**
![Carbon Tracking](https://github.com/user-attachments/assets/d3416e36-73c7-47d9-92b6-7a2aec92015a)

**Leader Board**
![Leaderboard](https://github.com/user-attachments/assets/2444a382-9401-4ccf-a217-18186af81193)

**Community Platform**
![Community Platform](https://github.com/user-attachments/assets/a782846f-c055-445d-be4b-98b5b24d00b5)



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
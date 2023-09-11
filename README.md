
Parent-Student School Progress Tracking System MVP specification
Tagline:Empowering Parents For Active Engagement in Their Child’s Education








Team
Developer: Emmanuel Otieno
Introduction
The Parent-Student School Progress Tracking System is a web-based application designed to provide parents with real-time access  and information to their child’s general progress.This will include academic progress, school-related news, fee tracking system and student-related assignments and resources.
Technologies
Python - The Backend Language
JavaScript - The Frontend Language
Flask - Web Development Framework
MySQL - Relational Database Management System
Mysql Workbench
HTML
CSS
Bootstrap framework

Infrastructure
Branching and Merging Process: The team will follow the "GitHub flow" branching model for the repository, ensuring code collaboration and code review before merging into the main branch.
Deployment Strategy: The project will utilize a CI/CD pipeline for automated testing and deployment to ensure seamless and reliable deployment to production.
Data Population: For testing and development, mock data and test fixtures will be used. For production, users will input their data through the user interface.
Testing Tools and Automation: The project will implement unit testing, integration testing, and end-to-end testing using Python's unittest, Selenium, or Cypress. Test automation will be integrated into the CI/CD pipeline.
Architecture






APIs and Methods
In the Parent-Student School Progress Tracking System, the web client communicates with the web server using various API routes. These enables data exchange and interaction between client and server components.Here are the main API routes and their associated methods:
/api/parent
GET: Retrieves parent information based on the provided parent ID.
POST: Creates a new parent profile using the provided data.
/api/student
GET: Fetches student details based on the provided student ID.
POST: Adds a new student to the system with the provided information.
/api/progress
GET: Retrieves academic progress data for a specific student, including exam results, grades, attendance, and teacher feedback.
POST: Allows teachers to update student progress data for a given academic period.
/api/news
GET: Fetches the latest news and announcements from the school.
POST: Enables school administrators to publish news and updates.
/api/fees
GET: Returns fee-related information for a specific student, including balance, payment history, and due dates.
POST: Allows parents to make fee payments and update payment information.
/api/assignments
GET: Retrieves assignment details for a specific student, including assignment descriptions, submission status, and deadlines.
POST: Enables teachers to create new assignments and update existing ones.
/api/messages
GET: Retrieves messages and communication history between parents, teachers, and administrators.
POST: Facilitates sending messages and communication between users.

APIs for External Clients:
User Management API:
User.register(username, email, password): Registers a new user with the provided username, email, and password.
User.login(email, password): Authenticates a user based on the provided email and password.
Student Information API:
Student.get_student_info(student_id): Fetches detailed information about a specific student based on the student ID.
Student.update_student_info(student_id, new_data): Allows external systems to update student information.
Parent-Teacher Communication API:
Communication.send_message(sender_id, recipient_id, message): Allows external systems to send messages between parents, teachers, and administrators.
Communication.get_messages(user_id): Retrieves the message history for a specific user.
3rd Party APIs:
Google Maps API:
Provides geolocation and mapping functionalities for locating the school and displaying its address to users.
Twilio API:
Enables sending SMS notifications and alerts to parents and students about important events, such as upcoming assignments or fee due dates.
Stripe API:
Integrates secure payment processing to handle fee payments made by parents through the application.

Data Model

User Stories

User Story 1: Parent Accesses Student Progress
As a parent, I want to view my child's academic progress, including grades, attendance, and teacher feedback,
So that I can monitor and support my child's educational journey effectively.
User Story 2: Parent Receives School Announcements
As a parent,
I want to receive school-related news and announcements,
So that I can stay informed about important events and activities in the school.
User Story 3: Parent Manages Fees and Payments
As a parent,
I want to check my child's fee balances, payment history, and upcoming due dates,
So that I can make timely fee payments and ensure my child's smooth participation in school activities.
User Story 4: Parent Tracks Student Assignments
As a parent,
I want to access my child's assignments, project deadlines, and teacher instructions,
So that I can actively engage in my child's learning process and help them manage their workload.
User Story 5: Parent-Teacher Communication
As a parent,
I want to exchange messages with my child's teachers,
So that I can communicate about their progress, concerns, and other important matters.

Objectives
The primary objective of Parent-Student School Progress Tracking System are as follows
Academic Progress Tracking:Provide Parents with access to their childs’s academic performance, including exam results,grades,attendance, and teacher’s feedback.In addition the parent can be always informed on general school results
News and Updates: Offers a news feed where school can post important announcements, events and academic updates keeping parents informed about school activities 
Fee Management: Enable parents to view fee balances, payment history, and upcoming fee due dates, facilitating timely fee payments
Assignment and Student related Resources :Allow parents to access their child’s assignment, project deadlines, and teacher instructions, fostering active involvement in the learning process .
Scope
The system will include the following features and functionalities:
Parent Registration
Parents will be able to register and create an account by providing their details and linking them to their child’s school records .
Academic Dashboard
A user-friendly dashboard for parents to view their child’s academic progress, including grades, attendance and teacher comments. 
News Feed
Offer a news feed where schools can post important announcements, events, and academic Updates, keeping parents informed about school activities.
Fee Management
A secure portal for parents to check their child’s balances, payment history, and receive notifications for upcoming fee dues.
Assignment and Resource Portal
An assignment tracking system that allows parents to view their child’s assignments, submission status and deadlines.
Communication
A messaging feature that enables direct communication between parents, teachers and school administrators.


Methodology
The development of the Parent-Student School Progress Tracking system will follow the following methodology
Requirement Gathering
Conduct interviews and surveys with parents,teachers and school administration to understand their need and expectation of the system.
System Design
Develop a comprehensive system architecture and design, outlining the user interface, database structure, and data flow.
Prototype Development
Build a functional prototype of the system to gather feedback and validate its usability.
Full-Scale Development
Develop the complete system with all the intended features and functionalities.
Testing and Validation
Conduct thorough testing to ensure the system's reliability, security, and usability.
Implementation and Deployment
Deploy the system on a secure web server, ensuring data privacy and access control.
Expected Outcomes
Improved Parent-Teacher Communication: The system will facilitate seamless communication between parents and teachers, leading to better support for students' academic progress.
Enhanced Parental Involvement: With easy access to academic information and assignments, parents can actively engage in their child's education.
Efficient Fee Management: Parents can conveniently view and manage fee-related information, promoting timely fee payments.
Enhanced Student Performance: The active involvement of parents in tracking their child's progress can positively impact students' academic performance and motivation.

What the system will not solve
The Parent-Student Tracking System does not replace direct communication between parents and teachers or substitute for face-to-face parent-teacher meetings. While it offers valuable insights into a child's academic performance, it does not replace personalized interactions with educators.
Users and Beneficiaries
The Parent-Student Tracking System will benefit parents, students, and educational institutions. Parents will have access to comprehensive data on their child's academic performance, enabling them to support their child's learning journey effectively. Students will be able to showcase their achievements through personalized portfolios, enhancing their self-expression and showcasing their talents. Educational institutions will experience improved parent engagement and satisfaction, leading to a stronger partnership between the school and parents.

Mockups



Locale Dependence
The Parent-Student Tracking System is designed to be adaptable to various educational institutions globally. While certain features may be localized based on language and currency, the core functionalities remain applicable to schools worldwide.
Risks
Technical Risks:
Data Security Breach: Implement robust security measures and regular audits to safeguard user data.
Scalability Challenges: Utilize cloud services with auto-scaling capabilities and optimize database queries to ensure performance.
Non-Technical Risks:
Legal and Compliance Risks: Conduct legal audits and obtain explicit user consent for data collection to comply with data protection laws.
User Content Quality: Implement a content review process to ensure the authenticity and appropriateness of user-submitted content.
User Engagement and Retention: Gather user feedback, update the platform regularly, and implement gamification elements to enhance user engagement.
Competitive Landscape: Emphasize unique features and remain updated with industry trends to stay competitive.
Existing Solutions
Online Portfolio Builders: Existing portfolio builders offer limited customization options and may lack specific features tailored to student portfolios.
Student Management Systems: Student management systems are primarily for administrative tasks and lack dedicated parent engagement features.
Educational Apps for Parents: Some educational apps provide insights into academic performance but may not offer comprehensive tracking and portfolio features.
Personal Finance Apps: Personal finance apps manage finances but lack fee balance tracking and academic progress monitoring.
Conclution
By developing the Parent-Student Tracking System, I aim to bridge the communication gap between parents and educational institutions, creating a more involved and supportive environment for students' growth and success. With a user-centric approach and robust technologies, I strive to deliver a valuable and intuitive platform for parents and students alike.



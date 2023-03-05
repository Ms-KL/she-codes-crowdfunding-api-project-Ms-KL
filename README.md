<img src="https://github.com/Ms-KL/Ms-KL/raw/main/images/shecodes-icon.png" width="80px" height="80px" />

# She Codes Plus Project 4: Crowdfunding Website (Back-End)

## About:

This is Crowdfunding Website was created by Kristy Leigh as a project for the [She Codes Plus](https://www.shecodes.com.au/) program.

- Visit deployed backend [HERE](https://icy-dew-540.fly.dev/)
- Visit deployed frontend: [HERE](https://prismatic-phoenix-20010b.netlify.app/)

### Tech & Skills Learned:

- Django
- Django REST Framework
- Python
- VS Code
- Github Desktop
- Deployment using Fly
- MVP Planning
- Database Schemas
- User Experience flowchart
- API Specifications
- Insomnia
  <br>

---

<br>

# Communitree

Welcome to Communitree, where tree-huggers gather to make a real impact on the urban forest of their community. Local Governments, schools and environmental organisations can create projects to raise funds for community busy bees and planting days/events. Supporters can pledge resources to help these projects.

<br>

---

## **TL:DR Links**

---

### **MVP Submission:**

- [Submission Document (Canva)](https://www.canva.com/design/DAFXgSq-5YI/VoGjxBH0387phr6s29IV1A/view?utm_content=DAFXgSq-5YI&utm_campaign=designshare&utm_medium=link&utm_source=publishshare)
- [User Flow-Chart (Figma)](https://www.figma.com/file/TTOAG3ee2VSnR9JWF2aG6l/Crowdfunding-Project?node-id=0%3A1&t=wOw8Y89TyRAGQ2p3-0)
- [GitHub MVP Submission Folder](https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-Ms-KL/tree/main/project_submission/MVP%20Submission)

### **Part A Submission:**

- [Deployed Project (Fly)](https://icy-dew-540.fly.dev/)
- [Submission Document (Canva)](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)
- [Insomnia Screenshots (Canva)](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#5)
- [GitHub Part A Submission Folder](https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-Ms-KL/tree/readme/project_submission/Part%20A%20Submission)

### **Part B Submission:**

- Please view the [ReadMe](https://github.com/Ms-KL/crowdfunding#readme) for Part B

---

## **Features**

---

See Also: [Project Requirements Checklist](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#2)

### **User Accounts**

- [x] Username
- [x] Email Address
- [x] Password

### **Project**

- [x] Create a project
  - [x] Title
  - [x] Owner (a user)
  - [x] Description
  - [x] Image
  - [x] Target Amount to Fundraise
  - [x] Open/Close (Accepting new supporters)
  - [x] When was the project created
- [x] Ability to pledge to a project
  - [x] An amount
  - [x] The project the pledge is for
  - [x] The supporter
  - [x] Whether the pledge is anonymous
  - [x] A comment to go with the pledge

### <b>Implement suitable update delete</b>

\*Note: Not all of these may be required for your project, if you have not included one of these please justify why.\*\*

- Project
  - [x] Create
  - [x] Retrieve
  - [x] Update
  - [x] Destroy
- Pledge
  - [x] Create
  - [x] Retrieve
  - [x] Update
  - [x] Destroy
- User
  - [x] Create
  - [x] Retrieve
  - [x] Update
  - [ ] Destroy -> _not required_
    - user can make themselves inactive. delete not activated to keep db integrity. Admin can still delete through admin portal.

### **Implement suitable permissions**

\*Note: Not all of these may be required for your project, if you have not included one of these please justify why.\*\*

- Project
  - [x] Limit who can create
  - [ ] Limit who can retrieve -> _not required_
  - [x] Limit who can update
  - [x] Limit who can delete
- Pledge
  - [x] Limit who can create
  - [ ] Limit who can retrieve -> _not required_
  - [x] Limit who can update -> _can only edit non-amount fields_
  - [x] Limit who can delete
- User
  - [ ] Limit who can retrieve -> _not required_
  - [x] Limit who can update
  - [x] Limit who can delete

### **Implement relevant status codes**

- [x] Get returns 200
- [x] Create returns 201
- [x] Not found returns 404

### **Handle failed requests gracefully**

- [x] 404 response returns JSON rather than text
  - Note: navigation to an unexpected page (eg: pledges/abc/) will return a custom text error message. However expected pages with no data to return yet (eg: pledges/100/) will return JSON

### **Use token authentication**

- [x] implement /api-token-auth/

---

## Additional features

---

See Also [MVP Submission - Features Page](https://www.canva.com/design/DAFXgSq-5YI/VoGjxBH0387phr6s29IV1A/view?utm_content=DAFXgSq-5YI&utm_campaign=designshare&utm_medium=link&utm_source=publishshare#11) | [Part A Submission - Features Page](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#10)

### **User Experience:**

- [x] { Filter Pledges and Projects }

{{ Filter pledges by supporter and project. Filter projects by is_open and owner. }}

- [x] { User Fields and History }

{{ First Name, Last Name, Bio and Avatar added. User Comments, Pledges and Projects history listed in Custom User Detail }}

- [x] { Change Password }

{{ Change password functionality added }}

- [x] { Comments }

{{ Comments feature added for users to interact with project }}

- [x] { Pledge and Comment History }

{{ Pledge and Comment List displayed in Project Detail }}

- [x] { Custom API Root }

{{ As per Ben's suggestion 02/02/23 }}

### **System Features:**

- [x] { Unique field value restrictions }

{{ project.title , user.email, user.username restricted; must be unique: throws integrity error with re-entry trigger if not unique }}

- [x] { Properties added }

{{ sum_pledge, goal_balance & funding_status added in Project Detail }}

### **External libraries used:**

- [x] django-filter

---

## Part A Submission

---

### **Links & Screenshots:**

- [x] A [link](https://icy-dew-540.fly.dev/) to the deployed project
- [x] A [screenshot](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#5) of Insomnia, demonstrating a successful GET method for any endpoint
- [x] A [screenshot](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#5) of Insomnia, demonstrating a successful POST method for any endpoint
- [x] A [screenshot](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#5) of Insomnia, demonstrating a token being returned
- [x] Your refined [API Specification (2 pages)](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#8) and [Database Schema](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#7).

### **Documentation:**

_Step by step [instructions](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#6) for how to register a new user and create a new project (i.e. endpoints and body data)._

1. Create User

```shell
    curl --request POST \
    --url https://icy-dew-540.fly.dev/users/ \
    --header 'Content-Type: application/json' \
    --data '{
        "username": "<insert_unique_username>",
        "email": "<insert_unique_email>",
        "password":"<insert_password>",
        "bio":"<insert_bio>",
        "avatar":"<insert_url_to_image>"
    }'
```

2. Sign in User

```shell
    curl --request POST \
    --url https://icy-dew-540.fly.dev/api-token-auth/ \
    --header 'Content-Type: application/json' \
    --data '{
        "username": "<insert_unique_username>",
        "password": "<insert_password>"
    }'
```

3. Create Project

```shell
    curl --request POST \
    --url https://icy-dew-540.fly.dev/projects/ \
    --header 'Content-Type: application/json' \
    --data '{
        "title": "<unique_title>",
        "description": "<project_description>",
        "goal": <integer>,
        "image": "<image_url>",
        "is_open": <boolean>,
        "date_created": "<auto_filled as today>"
    }'
```

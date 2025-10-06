I am a NetAcad Instructor Trying to teach network automation. I have attached our CCNA certification blueprint, I want you to generate an automation code based on the tasks in the blueprint. 
The Context I need you to follow:
- At most one Task for each topic 
- The code must be simple enough at an associate level 
- The code should not be completed allowing the students to fill in the blanks. 
- where there is a fill in the blanks line of code make sure you add a `TODO:` with instructions on what's needed to properly complete this line of code testing their basic automation and python knowledge 
- Upon completion, the automation scripts need to run successfully 
- CCNA blueprint can be found in the `assets` folder labeled `200-301-CCNA-v1.1.pdf` in this working directory 
- Yaml file labeled `devices.yaml` can be found in the `assets folder` , this is an export of the topology used in our CML Lab. for all examples that will need access to a device, leverage the config defined in the Yaml file. 

Requirements:
1. IOS commands should be read-only
2. use `R3` router for the tasks
3. Never change device configuration
4. Generate a `solution` folder with the completed tasks for the Instructors to use

Constraints:
- only use native RESTCONF models
- A task should be around pulling RESTCONF interfaces 
- Another Task should be around Parsing interfaces from RESTCONF service as JSON
- Do Not parse YAML files
- Netmiko task is within scope
- Jinja Templating is out of scope
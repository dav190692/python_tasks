#part one
# def c3_linearization(class_hierarchy):
#     if not class_hierarchy:
#         return []

#     mro = []
#     while True:
#         non_empty_lists = [h for h in class_hierarchy if h]
        
#         if not non_empty_lists:
#             break

#         heads = {h[0] for h in non_empty_lists}
        
#         found = None
#         for head in heads:
#             if all(head not in t[1:] for t in non_empty_lists):
#                 found = head
#                 break
#         if found is None:
#             raise ValueError("Wrong hierarchy")

#         mro.append(found)
#         for lst in non_empty_lists:
#             if lst[0] == found:
#                 lst.pop(0)
            

#     return mro


# class_hierarchy1 = [
#     ['A', 'B', 'C', 'D','E'],
#     ['B', 'D'],
#     ['C', 'D', 'E'],
# ]
# print(c3_linearization(class_hierarchy1)) 

# class_hierarchy2 = [
#     ['A', 'B', 'C'],
#     ['B', 'D', 'A'],
#     ['C', 'D', ],
# ]
# print(c3_linearization(class_hierarchy2)) 


##############################################################################################################
#part two start






# class LoggerMixin:
#     def log(self, message):
#         print(f"[{self.__class__.__name__}] : {message}")


# class EmailNotifierMixin:
#     def send_email_notification(self, message):
#         print(f"Email notification sent :  {message}")

# class InAppNotifierMixin:
#     def send_app_notification(self, message):
#         print(f"In-app notification sent :  {message}")

# class PushNotifierMixin:
#     def send_push_notification(self, message):
#         print(f"Push notification sent :  {message}")


# class ProjectManager(LoggerMixin, EmailNotifierMixin, InAppNotifierMixin, PushNotifierMixin):
#     def __init__(self, manager_name):
#         super().__init__()
#         self.manager_name = manager_name

#     @property
#     def manager_name(self):
#         return self.__manager_name
    
#     @manager_name.setter
#     def manager_name(self, value):
#         if not value or not isinstance(value, str):
#             raise ValueError('Please write correct value for manager name')
#         self.__manager_name = value

#     def manager_notifier(self, message):
#         self.send_app_notification(message)
#         self.send_email_notification(message)
#         self.send_push_notification(message)


# class TeamMember(LoggerMixin, InAppNotifierMixin, PushNotifierMixin):
#     def __init__(self, team_member_name):
#         super().__init__()
#         self.team_member_name = team_member_name

#     @property
#     def team_member_name(self):
#         return self.__team_member_name
    
#     @team_member_name.setter
#     def team_member_name(self, value):
#         if not value or not isinstance(value, str):
#             raise ValueError('Please type correct value for team member name')
#         self.__team_member_name = value

#     def team_member_notifier(self, message):
#         self.send_app_notification(message)
#         self.send_push_notification(message)


        

# class User(LoggerMixin):
#     def __init__(self, name, age, email,) -> None:
#         self.name = name
#         self.age = age
#         self.email = email

#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, value):
#         if value == "" or  not isinstance(value, str):
#             raise ValueError('please type corect value for name')
#         else: 
#             self.__name = value

#     @property       
#     def age(self):
#         return self.__age     
    
#     @age.setter
#     def age(self, value):
#         if value < 0 or not isinstance(value, int):
#             raise ValueError('please write corect value for age') 
#         self.__age = value
        
        

#     @property
#     def email(self):
#         return self.__email
    

#     @email.setter
#     def email(self, value):
#         if value == "" or not isinstance(value, str):
#             raise ValueError('please type corect value for email')
#         self.__email = value

# class ExternalContractor(User):
#     def __init__(self, name, age, email):
#         super().__init__(name, age, email)
#         self.team_member = TeamMember(name)
#         self.project_manager = ProjectManager(name)



# if __name__ == "__main__":    
#     # user
#     user1 = User("Davit", 31, "dav190692@gmail.com")
#     user1.log('User Davit created')

#     # project manager
#     project_manager1 = ProjectManager("Lilit")
#     project_manager1.log("Project manager Lilit created")
#     project_manager1.manager_notifier("New project")

#     # team member
#     team_member1 = TeamMember("Mariam")
#     team_member1.log("Team member Mariam created")
#     team_member1.team_member_notifier("Update!!!!!!")

#     # ExternalContractor

#     external_contractor = ExternalContractor("Vahan", 78, "Vahan@gmail.com")
#     external_contractor.log("external contractor Vahan created")
#     external_contractor.project_manager.manager_notifier(" manager external_contractor")
#     external_contractor.team_member.team_member_notifier("team-member external_contractor")




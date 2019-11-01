class Versions:
  def __init__(self,version):
    #init the object
    self.versionMap = version.split('.')

  #the function compares the version with another passed to it by looping through the
  #array and see if any of the numbers with similar index is greater or less the function is O(N) time
  def compare(self,version):
    current = self.versionMap
    compareWith = version.versionMap
 
    itter = len(current)
    # check if they are the same
    if current == compareWith:
      return {
               'message':'Same version'
            }

    try:
      for i in range(itter):
        # print(current[i], compareWith[i],'\n')

      
          if current[i] < compareWith[i]:
            return {
              'status':True,
              'message':'This version is greater than me'
            }
        
          elif current[i] > compareWith[i]:
             return {
              'status':False,
              'message':'This version is less than me'
            }

          else:
            #this is if current[i] == compareWith[i] i would like it to go to the next item
            pass
      
      return {
            'status':True,
            'message':'This version is Greater than me and  longer'
          }
    
     
    except:
        # means it is longer than the copared version
        return {
            'status':False,
            'message':'This version is Less than me  longer'
          }

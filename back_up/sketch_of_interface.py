from abc import ABC, abstractmethod

class Project_interface(ABC):
    
    # need or not?
    #def __init__(self, value):
    #    self.value = value
    #    super().__init__()
    
    # method for import the data
    @abstractmethod
    def import_data(self):
        pass
    
    # method for set variables (constant, etc.)
    @abstractmethod
    def set_variables(self):
        pass
    
    # method for plot graphics
    @abstractmethod
    def plot(self):
        pass
    
    # method for preprocessing data
    # maybe can include data augmentation?
    @abstractmethod
    def preprocessing_data(self):
        pass
    
    # method for initialization model
    @abstractmethod
    def init_model(self):
        pass
    
    # method for train model
    @abstractmethod
    def train_model(self):
        pass
    
    # method for split dataset on train|test|val sets
    @abstractmethod
    def split_on_train_test_val_sets(self):
        pass
    
    # method for predict
    @abstractmethod
    def predict(self):
        pass




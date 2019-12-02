
# -*- coding: utf-8 -*-

from remi.gui import *
from remi import start, App


class untitled(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(untitled, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return untitled.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        MainContainer = Container()
        MainContainer.attributes.update({"class":"Container","editor_constructor":"()","editor_varname":"MainContainer","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Container"})
        MainContainer.style.update({"margin":"0px","width":"375.0px","height":"465.0px","top":"75.0px","left":"150.0px","position":"absolute"})
        TitleLabel = Label('Audio Processing')
        TitleLabel.attributes.update({"class":"Label","editor_constructor":"('Audio Processing')","editor_varname":"TitleLabel","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Label"})
        TitleLabel.style.update({"margin":"0px","width":"135.0px","height":"30.0px","top":"15.0px","left":"120.0px","position":"absolute"})
        MainContainer.append(TitleLabel,'TitleLabel')
        filesSelectBox = DropDown()
        filesSelectBox.attributes.update({"class":"DropDown","editor_constructor":"()","editor_varname":"filesSelectBox","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"DropDown"})
        filesSelectBox.style.update({"margin":"0px","width":"180.0px","height":"30.0px","top":"60.0px","left":"165.0px","position":"absolute"})
        MainContainer.append(filesSelectBox,'filesSelectBox')
        SelectFileLabel = Label('Select a file')
        SelectFileLabel.attributes.update({"class":"Label","editor_constructor":"('Select a file')","editor_varname":"SelectFileLabel","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Label"})
        SelectFileLabel.style.update({"margin":"0px","width":"100px","height":"30px","top":"60.0px","left":"30.0px","position":"absolute"})
        MainContainer.append(SelectFileLabel,'SelectFileLabel')
        recordButton = Button('Rec')
        recordButton.attributes.update({"class":"Button","editor_constructor":"('Rec')","editor_varname":"recordButton","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Button"})
        recordButton.style.update({"margin":"0px","width":"100px","height":"30px","top":"105.0px","left":"240.0px","position":"absolute"})
        MainContainer.append(recordButton,'recordButton')
        InterpolateSpinBox = SpinBox(0,0,0,1)
        InterpolateSpinBox.attributes.update({"class":"number","value":"0","type":"number","autocomplete":"off","min":"0","max":"0","step":"1","editor_constructor":"(0,0,0,1)","editor_varname":"InterpolateSpinBox","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"SpinBox"})
        InterpolateSpinBox.style.update({"margin":"0px","width":"60.0px","height":"30.0px","top":"165.0px","left":"210.0px","position":"absolute"})
        MainContainer.append(InterpolateSpinBox,'InterpolateSpinBox')
        InterpolateBtn = Button('Interpolate')
        InterpolateBtn.attributes.update({"class":"Button","editor_constructor":"('Interpolate')","editor_varname":"InterpolateBtn","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Button"})
        InterpolateBtn.style.update({"margin":"0px","width":"100px","height":"30px","top":"165.0px","left":"30.0px","position":"absolute"})
        MainContainer.append(InterpolateBtn,'InterpolateBtn')
        DecimateBtn = Button('Decimate')
        DecimateBtn.attributes.update({"class":"Button","editor_constructor":"('Decimate')","editor_varname":"DecimateBtn","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Button"})
        DecimateBtn.style.update({"margin":"0px","width":"100px","height":"30px","top":"225.0px","left":"30.0px","position":"absolute"})
        MainContainer.append(DecimateBtn,'DecimateBtn')
        InterpolateLabel = Label('Factor:')
        InterpolateLabel.attributes.update({"class":"Label","editor_constructor":"('Factor:')","editor_varname":"InterpolateLabel","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Label"})
        InterpolateLabel.style.update({"margin":"0px","width":"45.0px","height":"30.0px","top":"165.0px","left":"150.0px","position":"absolute","align-items":"center","align-content":"center","align-self":"center"})
        MainContainer.append(InterpolateLabel,'InterpolateLabel')
        LabelDecimate = Label('Factor:')
        LabelDecimate.attributes.update({"class":"Label","editor_constructor":"('Factor:')","editor_varname":"LabelDecimate","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Label"})
        LabelDecimate.style.update({"margin":"0px","width":"100px","height":"30px","top":"225.0px","left":"150.0px","position":"absolute"})
        MainContainer.append(LabelDecimate,'LabelDecimate')
        DecimateSpinBox = SpinBox(0,0,0,1)
        DecimateSpinBox.attributes.update({"class":"number","value":"0","type":"number","autocomplete":"off","min":"0","max":"0","step":"1","editor_constructor":"(0,0,0,1)","editor_varname":"DecimateSpinBox","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"SpinBox"})
        DecimateSpinBox.style.update({"margin":"0px","width":"60.0px","height":"30.0px","top":"225.0px","left":"210.0px","position":"absolute"})
        MainContainer.append(DecimateSpinBox,'DecimateSpinBox')
        

        self.MainContainer = MainContainer
        return self.MainContainer
    


#Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])

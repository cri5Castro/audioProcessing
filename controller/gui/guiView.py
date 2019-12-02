
# -*- coding: utf-8 -*-
import glob,os
import threading
from remi.gui import *
from remi import start, App


class MainWindow(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(MainWindow, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return MainWindow.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        MainContainer = Container()
        MainContainer.attributes.update({"class":"Container","editor_constructor":"()","editor_varname":"MainContainer","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Container"})
        MainContainer.style.update({"margin":"0px","width":"360.0px","height":"465.0px","top":"75.0px","left":"165.0px","position":"absolute"})
        TitleLabel = Label('Audio Processing')
        TitleLabel.attributes.update({"class":"Label","editor_constructor":"('Audio Processing')","editor_varname":"TitleLabel","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Label"})
        TitleLabel.style.update({"margin":"0px","width":"135.0px","height":"30.0px","top":"15.0px","left":"120.0px","position":"absolute","font-weight":"bold"})
        MainContainer.append(TitleLabel,'TitleLabel')
        filesSelectBox = DropDown.new_from_list(glob.glob('*.wav'))
        filesSelectBox.style.update({"margin":"0px","width":"180.0px","height":"30.0px","top":"75.0px","left":"30.0px","position":"absolute"})
        MainContainer.append(filesSelectBox,'filesSelectBox')
        SelectFileLabel = Label('Select a file')
        SelectFileLabel.attributes.update({"class":"Label","editor_constructor":"('Select a file')","editor_varname":"SelectFileLabel","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Label"})
        SelectFileLabel.style.update({"margin":"0px","width":"90.0px","height":"30.0px","top":"45.0px","left":"45.0px","position":"absolute"})
        MainContainer.append(SelectFileLabel,'SelectFileLabel')
        recordButton = Button('Rec')
        recordButton.attributes.update({"class":"Button","editor_constructor":"('Rec')","editor_varname":"recordButton","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Button"})
        recordButton.style.update({"margin":"0px","width":"100px","height":"30px","top":"120.0px","left":"225.0px","position":"absolute"})
        MainContainer.append(recordButton,'recordButton')
        InterpolateSpinBox = SpinBox(0,0,10,1)
        InterpolateSpinBox.attributes.update({"class":"number","value":"0","type":"number","autocomplete":"off","min":"0","max":"10","step":"1","editor_constructor":"(0,0,10,1)","editor_varname":"InterpolateSpinBox","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"SpinBox"})
        InterpolateSpinBox.style.update({"margin":"0px","width":"75.0px","height":"30.0px","top":"180.0px","left":"210.0px","position":"absolute"})
        MainContainer.append(InterpolateSpinBox,'InterpolateSpinBox')
        InterpolateBtn = Button('Interpolate')
        InterpolateBtn.attributes.update({"class":"Button","editor_constructor":"('Interpolate')","editor_varname":"InterpolateBtn","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Button"})
        InterpolateBtn.style.update({"margin":"0px","width":"100px","height":"30px","top":"180.0px","left":"30.0px","position":"absolute"})
        MainContainer.append(InterpolateBtn,'InterpolateBtn')
        DecimateBtn = Button('Decimate')
        DecimateBtn.attributes.update({"class":"Button","editor_constructor":"('Decimate')","editor_varname":"DecimateBtn","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Button"})
        DecimateBtn.style.update({"margin":"0px","width":"100px","height":"30px","top":"225.0px","left":"30.0px","position":"absolute"})
        MainContainer.append(DecimateBtn,'DecimateBtn')
        InterpolateLabel = Label('Factor:')
        InterpolateLabel.attributes.update({"class":"Label","editor_constructor":"('Factor:')","editor_varname":"InterpolateLabel","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Label"})
        InterpolateLabel.style.update({"margin":"0px","width":"45.0px","height":"30.0px","top":"180.0px","left":"150.0px","position":"absolute","align-items":"center","align-content":"center","align-self":"center"})
        MainContainer.append(InterpolateLabel,'InterpolateLabel')
        LabelDecimate = Label('Factor:')
        LabelDecimate.attributes.update({"class":"Label","editor_constructor":"('Factor:')","editor_varname":"LabelDecimate","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Label"})
        LabelDecimate.style.update({"margin":"0px","width":"100px","height":"30px","top":"225.0px","left":"150.0px","position":"absolute"})
        MainContainer.append(LabelDecimate,'LabelDecimate')
        DecimateSpinBox = SpinBox(0,0,10,1)
        DecimateSpinBox.attributes.update({"class":"number","value":"0","type":"number","autocomplete":"off","min":"0","max":"10","step":"1","editor_constructor":"(0,0,10,1)","editor_varname":"DecimateSpinBox","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"SpinBox"})
        DecimateSpinBox.style.update({"margin":"0px","width":"75.0px","height":"30.0px","top":"225.0px","left":"210.0px","position":"absolute"})
        MainContainer.append(DecimateSpinBox,'DecimateSpinBox')
        PlayBtn = Button('Play')
        PlayBtn.attributes.update({"class":"Button","editor_constructor":"('Play')","editor_varname":"PlayBtn","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Button"})
        PlayBtn.style.update({"margin":"0px","width":"100px","height":"30px","top":"75.0px","left":"225.0px","position":"absolute"})
        MainContainer.append(PlayBtn,'PlayBtn')
        ShiftLabel = Label('Factor:')
        ShiftLabel.attributes.update({"class":"Label","editor_constructor":"('Factor:')","editor_varname":"ShiftLabel","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Label"})
        ShiftLabel.style.update({"margin":"0px","width":"45.0px","height":"30.0px","top":"270.0px","left":"150.0px","position":"absolute"})
        MainContainer.append(ShiftLabel,'ShiftLabel')
        ShiftSpinBox = SpinBox(0,-200000,200000,1)
        ShiftSpinBox.attributes.update({"class":"number","value":"0","type":"number","autocomplete":"off","min":"-200000","max":"200000","step":"1","editor_constructor":"(0,-200000,200000,1)","editor_varname":"ShiftSpinBox","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"SpinBox"})
        ShiftSpinBox.style.update({"margin":"0px","width":"75.0px","height":"30.0px","top":"270.0px","left":"210.0px","position":"absolute"})
        MainContainer.append(ShiftSpinBox,'ShiftSpinBox')
        ShiftBtn = Button('Shift')
        ShiftBtn.attributes.update({"class":"Button","editor_constructor":"('Shift')","editor_varname":"ShiftBtn","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Button"})
        ShiftBtn.style.update({"margin":"0px","width":"100px","height":"30px","top":"270.0px","left":"30.0px","position":"absolute"})
        MainContainer.append(ShiftBtn,'ShiftBtn')
        ReflectBtn = Button('Reflect')
        ReflectBtn.attributes.update({"class":"Button","editor_constructor":"('Reflect')","editor_varname":"ReflectBtn","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Button"})
        ReflectBtn.style.update({"margin":"0px","width":"100px","height":"30px","top":"360.0px","left":"30.0px","position":"absolute"})
        MainContainer.append(ReflectBtn,'ReflectBtn')
        ModulateBtn = Button('Modulate')
        ModulateBtn.attributes.update({"class":"Button","editor_constructor":"('Modulate')","editor_varname":"ModulateBtn","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Button"})
        ModulateBtn.style.update({"margin":"0px","width":"100px","height":"30px","top":"315.0px","left":"30.0px","position":"absolute"})
        MainContainer.append(ModulateBtn,'ModulateBtn')
        ModulateLbl = Label('Factor:')
        ModulateLbl.attributes.update({"class":"Label","editor_constructor":"('Factor:')","editor_varname":"ModulateLbl","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Label"})
        ModulateLbl.style.update({"margin":"0px","width":"45.0px","height":"30.0px","top":"315.0px","left":"150.0px","position":"absolute"})
        MainContainer.append(ModulateLbl,'ModulateLbl')
        SpinBoxModulate = SpinBox(0,-10000,10000,0)
        SpinBoxModulate.attributes.update({"class":"number","value":"0","type":"number","autocomplete":"off","min":"-10000","max":"10000","step":"0","editor_constructor":"(0,-10000,10000,0)","editor_varname":"SpinBoxModulate","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"SpinBox"})
        SpinBoxModulate.style.update({"margin":"0px","width":"75.0px","height":"30.0px","top":"315.0px","left":"210.0px","position":"absolute"})
        MainContainer.append(SpinBoxModulate,'SpinBoxModulate')
        PlotBtn = Button('Plot')
        PlotBtn.attributes.update({"class":"Button","editor_constructor":"('Plot')","editor_varname":"PlotBtn","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Button"})
        PlotBtn.style.update({"margin":"0px","width":"100px","height":"30px","top":"420.0px","left":"30.0px","position":"absolute"})
        MainContainer.append(PlotBtn,'PlotBtn')
        MainContainer.children['recordButton'].onclick.do(self.onclick_recordButton)
        MainContainer.children['InterpolateBtn'].onclick.do(self.onclick_InterpolateBtn)
        MainContainer.children['DecimateBtn'].onclick.do(self.onclick_DecimateBtn)
        MainContainer.children['PlayBtn'].onclick.do(self.onclick_PlayBtn)
        MainContainer.children['ShiftBtn'].onclick.do(self.onclick_ShiftBtn)
        MainContainer.children['ReflectBtn'].onclick.do(self.onclick_ReflectBtn)
        MainContainer.children['ModulateBtn'].onclick.do(self.onclick_ModulateBtn)
        MainContainer.children['PlotBtn'].onclick.do(self.onclick_PlotBtn)
        self.MainContainer = MainContainer
        return self.MainContainer
    
    def onclick_recordButton(self, emitter):
        instruction = 'python -m controller record -p True'
        self.MainContainer.children['filesSelectBox'].set_value('record.wav')
        os.system(instruction)

    def onclick_InterpolateBtn(self, emitter):
        ipath=self.MainContainer.children['filesSelectBox'].get_value()
        factor=self.MainContainer.children['InterpolateSpinBox'].get_value()
        instruction = 'python -m controller interpolate '+ipath+' ' + factor +' -p True'
        os.system(instruction)

    def onclick_DecimateBtn(self, emitter):
        ipath=self.MainContainer.children['filesSelectBox'].get_value()
        factor=self.MainContainer.children['DecimateSpinBox'].get_value()
        instruction = 'python -m controller decimate '+ipath+' ' + factor +' -p True'
        os.system(instruction)

    def onclick_PlayBtn(self, emitter):
        ipath=self.MainContainer.children['filesSelectBox'].get_value()
        instruction = 'python -m controller play '+ipath+' -p True'
        os.system(instruction)
        
    def onclick_ShiftBtn(self, emitter):
        ipath=self.MainContainer.children['filesSelectBox'].get_value()
        factor=self.MainContainer.children['ShiftSpinBox'].get_value()
        instruction = 'python -m controller shift '+ipath+' ' + factor +' -p True'
        os.system(instruction)

    def onclick_ReflectBtn(self, emitter):
        ipath=self.MainContainer.children['filesSelectBox'].get_value()
        instruction = 'python -m controller reflect '+ipath
        os.system(instruction)

    def onclick_ModulateBtn(self, emitter):
        ipath=self.MainContainer.children['filesSelectBox'].get_value()
        factor=self.MainContainer.children['SpinBoxModulate'].get_value()
        instruction = 'python -m controller mamp '+ipath+' ' + factor +' -p True'
        os.system(instruction)

    def onclick_PlotBtn(self, emitter):
        ipath=self.MainContainer.children['filesSelectBox'].get_value()
        instruction = 'python -m controller plot '+ipath
        os.system(instruction)
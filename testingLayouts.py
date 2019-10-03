diccionario_try = {'nombre':'int', 'gato':'float', 'que':'text'}  
import functools
class window_ui():
    def __init__(self):
        self.diccionario_try = {} 
        self.ventanaNombre = 'myWindowID'
        self.Titulo = 'Autorig Builder'
        self.Alto = 350
        self.Ancho = 500
        if cmds.window(self.ventanaNombre, exists=True):
            cmds.deleteUI(self.ventanaNombre)
        self.VENTANA = cmds.window(self.ventanaNombre, title='AutorigBuilder', width=self.Alto, height = self.Ancho)
   
    def layout_creator(self, input_dic = None, *pArgs):
        extracted_dic = input_dic  
        for element in extracted_dic:   
            input_kind = input_dic.get(element)     
            cmds.text(label = element)
            if input_kind == 'float':
                cmds.floatField()
            elif input_kind == 'int':
                cmds.intField()
            elif input_kind == 'text':
                cmds.textField()    
  
  
  
  
    def tryDic1(self, *pArgs):
        self.diccionario_try = {'nombre':'int', 'gato':'float', 'que':'text'}  
        return self.diccionario_try
    
    def tryDic2(self, *pArgs):
        self.diccionario_try = {'what':'int', 'about':'float', 'it':'text'} 
        return self.diccionario_try 
    
    def modular_interface(self):        

        self.scrollLayout = cmds.scrollLayout()
        self.master_layout = cmds.rowLayout('master_layout', numberOfColumns=2)
        cmds.rowColumnLayout(numberOfColumns=1, columnOffset=[(1, 'right', 3) ], parent = self.master_layout)
        cmds.button(label='Close Rig', command= functools.partial(self.layout_creator, self.tryDic1()), w=100, h=20)
        cmds.button(label='Close Rig', command = functools.partial(self.layout_creator, self.tryDic2()), w=100, h=20)
        cmds.button(label='Close Rig', w=100, h=20)
        
        self.modular_layout = cmds.rowColumnLayout('modular_layout', numberOfColumns=2, columnOffset=[(1, 'right', 3) ], parent = self.master_layout, ut=True)
        modular_layout = self.modular_layout
        def clearLayout(layout_del = modular_layout):
            while layout_del.count(*pArgs):
                child = layout_del.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout_del() is not None:
                    clearLayout(child.layout_del()) 
                    
        clearLayout(modular_layout)                
        self.layout_creator(self.diccionario_try)
        cmds.showWindow()
        
        
test = window_ui()  

test.modular_interface()
              
        

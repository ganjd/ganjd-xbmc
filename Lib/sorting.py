

from PyQt4.QtCore import QObject



class Sort(QObject):
    
    def __init__(self, treeWidget):
        QObject.__init__(self)
        
        self.treeWidget = treeWidget
        
    
    
    def byColumn(self, int):
        treeWidget = self.treeWidget
        
        order = treeWidget.header().sortIndicatorOrder()
        columnText = treeWidget.headerItem().text(int)
        count = treeWidget.topLevelItemCount()

        #Datum
        if columnText == 'Datum':
            lst = []
            for i in range(0, count):
                dict = {}
                item = treeWidget.topLevelItem(i)
                text = item.text(0)
                dict['date'] = str(text)
                dict['item'] = item
                dict['id'] = i
                lst.append(dict)
                
            for i in range(0, count):
                treeWidget.takeTopLevelItem(0)
    
            import datetime
            lst.sort(key=lambda x: datetime.datetime.strptime(x['date'], '%d.%m.%Y'))
            if order == 0:
                lst.reverse()
            
            for i, s in enumerate(lst):
                item = treeWidget.topLevelItem(s['id'])
                treeWidget.insertTopLevelItem(i, s['item'])
                
        #Stunden
        elif columnText == 'Stunden':
            lst = []
            for i in range(0, count):
                dict = {}
                item = treeWidget.topLevelItem(i)
                text = item.text(int)
                dict['stunden'] = str(text)
                dict['item'] = item
                dict['id'] = i
                lst.append(dict)
                
            for i in range(0, count):
                treeWidget.takeTopLevelItem(0)
                
            lst.sort(key=lambda x: float(x['stunden']))
            if order == 1:
                lst.reverse()
            
            for i, s in enumerate(lst):
                item = treeWidget.topLevelItem(s['id'])
                treeWidget.insertTopLevelItem(i, s['item'])
        
        #Betrag
        elif columnText == 'Betrag':
            lst = []
            for i in range(0, count):
                dict = {}
                item = treeWidget.topLevelItem(i)
                text = item.text(int)
                betrag = text.replace(',', '.')
                dict['betrag'] = str(betrag)
                dict['item'] = item
                dict['id'] = i
                lst.append(dict)
                
            for i in range(0, count):
                treeWidget.takeTopLevelItem(0)
                
            lst.sort(key=lambda x: float(x['betrag']))
            if order == 1:
                lst.reverse()
            
            for i, s in enumerate(lst):
                item = treeWidget.topLevelItem(s['id'])
                treeWidget.insertTopLevelItem(i, s['item'])
        
        #Standard Order
        else:
            treeWidget.sortItems(int, order)
        

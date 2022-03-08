import ui
import player
import mouseModule
import net
import app
import chat
import snd
import item
import grp
import uiScriptLocale
import localeInfo
import ime
import grpText
import uiToolTip

import os
import localegame
import gameInfo
import event
import uiPickMoney
import wndMgr

Item_Slot_Eklenen = 0

DUELLO_START = 0
SEND_START = 0
ItemSlot_Benim = []
ItemSlot_Benim2 = []
ItemSlot_R_Ekle = ""
ItemSlot_R_Ekle_Ekipman = ""
ItemSlot = []
ItemEkle_DURUM = 0
ItemEkle_DURUM_Ekipman = 0

class itemineduello(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.wndEquip = None
		self.tokens = None		
		self.activeslot = 1
		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.Hide()
		self.saveName = "lib/"+str(player.GetName())+"1.ddr"

		self.ItemSlotList = {}
		self.ItemSlotList_Ekipman = {}
		self.ItemSlotList_R = {}
		self.ItemSlotList_R_Ekipman = {}
		self.ItemSlotList_R_I = {}
		self.ItemSlotList_R_I_Ekipman = {}
		self.ItemSlot = []
		self.ItemSlot_Ekipman = []
		self.kapat = 0
		self.param = 0

		self.dlgPickMoney = Duello_para_ayarlari()
		self.dlgPickMoney.LoadDialog()
		self.dlgPickMoney.Hide()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		global ItemSlot
		global DUELLO_START
		global SEND_START
		global ItemSlot_Benim
		global ItemSlot_Benim2
		global ItemSlot_R_Ekle
		global ItemSlot_R_Ekle_Ekipman
		global ItemSlot
		global ItemEkle_DURUM
		global ItemEkle_DURUM_Ekipman
		self.__LoadWindow()
		self.SetCenterPosition()
		ui.ScriptWindow.Show(self)

		self.param = int(player.GetElk())
		gameInfo.DUELLO_RAKIP_PARA = 0
		gameInfo.DUELLO_BENIM_PARA = 0
		gameInfo.DUELLO_KABUL = 0
		gameInfo.DUELLO_KABUL_RAKIP = 0

		gameInfo.DUELLO_ROUND = 1
		gameInfo.DUELLO_ROUND_BASLAT = 0
		gameInfo.DUELLO_ROUND_ZAMAN_IN = 0
		gameInfo.DUELLO_ROUND_ZAMAN_KALAN = 0
		gameInfo.DUELLO_ROUND_DURUM = 0
		gameInfo.DUELLO_SKOR_MY = 0
		gameInfo.DUELLO_SKOR_TARGET = 0
		gameInfo.DUELLO_KAPAT = 0

		self.kapat = 0
		self.ItemSlotList = {}
		self.ItemSlotList_Ekipman = {}
		self.ItemSlotList_R = {} ## Rakibin Item Listesi ##
		self.ItemSlotList_R_Ekipman = {} ## Rakibin Ekipman Item Listesi ##
		self.ItemSlotList_R_I = {}
		self.ItemSlotList_R_I_Ekipman = {}
		self.ItemSlot = []
		self.ItemSlot_Ekipman = []

		DUELLO_START = 0
		SEND_START = 0
		ItemSlot_Benim = []
		ItemSlot_Benim2 = []
		ItemSlot_R_Ekle = ""
		ItemSlot_R_Ekle_Ekipman = ""
		ItemSlot = []
		ItemEkle_DURUM = 0
		ItemEkle_DURUM_Ekipman = 0
		
	def Close2(self):
		global DUELLO_START
		global SEND_START
		global ItemSlot_Benim
		global ItemSlot_Benim2
		global ItemSlot_R_Ekle
		global ItemSlot_R_Ekle_Ekipman
		global ItemSlot
		global ItemEkle_DURUM
		global ItemEkle_DURUM_Ekipman
		
		if self.kapat == 0:
			net.SendWhisperPacket(gameInfo.DUELLO_RAKIP, "#xsbyfatihbab34dsadsanxsadadsadaafsafafsxasxawqwqdsaafafasfafsafafsafsa#")
			
		#if gelen==1:
		gameInfo.PYTHONISLEM="itemine_duello_sil#"+str(gameInfo.DUELLO_RAKIP)
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		
		self.roundWindow.Hide()
		gameInfo.DUELLO_ROUND = 1
		gameInfo.DUELLO_ROUND_BASLAT = 0
		gameInfo.DUELLO_ROUND_ZAMAN_IN = 0
		gameInfo.DUELLO_ROUND_ZAMAN_KALAN = 0
		gameInfo.DUELLO_ROUND_DURUM = 0
		gameInfo.DUELLO_SKOR_MY = 0
		gameInfo.DUELLO_SKOR_TARGET = 0
		gameInfo.DUELLO_DURUM = 0
		gameInfo.DUELLO_VID = 0
		gameInfo.DUELLO_BASLATAN = 0
		gameInfo.DUELLO_RAKIP_PARA = 0
		gameInfo.DUELLO_BENIM_PARA = 0
		gameInfo.DUELLO_KABUL = 0
		gameInfo.DUELLO_KABUL_RAKIP = 0
		if "#"+str(gameInfo.DUELLO_RAKIP)+"#" in gameInfo.DUELLO_YOLLAYANLAR:
			gameInfo.DUELLO_YOLLAYANLAR.remove("#"+str(gameInfo.DUELLO_RAKIP)+"#")
		
		if "#"+str(gameInfo.DUELLO_RAKIP)+"#" in gameInfo.DUELLO_YOLLANANLAR:
			gameInfo.DUELLO_YOLLANANLAR.remove("#"+str(gameInfo.DUELLO_RAKIP)+"#")

		gameInfo.DUELLO_RAKIP = ""
		gameInfo.DUELLO_KAPAT = 0

		self.kapat = 0
		self.ItemSlotList = {}
		self.ItemSlotList_Ekipman = {}
		self.ItemSlotList_R = {} ## Rakibin Item Listesi ##
		self.ItemSlotList_R_Ekipman = {} ## Rakibin Ekipman Item Listesi ##
		self.ItemSlotList_R_I = {}
		self.ItemSlotList_R_I_Ekipman = {}
		self.ItemSlot = []
		self.ItemSlot_Ekipman = []

		DUELLO_START = 0
		SEND_START = 0
		ItemSlot_Benim = []
		ItemSlot_Benim2 = []
		ItemSlot_R_Ekle = ""
		ItemSlot_R_Ekle_Ekipman = ""
		ItemSlot = []
		ItemEkle_DURUM = 0
		ItemEkle_DURUM_Ekipman = 0

		self.Hide()

	def Close(self,gelen=0):
		global DUELLO_START
		global SEND_START
		global ItemSlot_Benim
		global ItemSlot_Benim2
		global ItemSlot_R_Ekle
		global ItemSlot_R_Ekle_Ekipman
		global ItemSlot
		global ItemEkle_DURUM
		global ItemEkle_DURUM_Ekipman
		
		if self.kapat == 0:
			net.SendWhisperPacket(gameInfo.DUELLO_RAKIP, "#xsbyfatihbab34dsadsanxsadadsadaafsafafsxasxawqwqdsaafafasfafsafafsafsa#")
			
		#if gelen==1:
		gameInfo.PYTHONISLEM="itemine_duello_sil#"+str(gameInfo.DUELLO_RAKIP)
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		
		self.roundWindow.Hide()
		gameInfo.DUELLO_ROUND = 1
		gameInfo.DUELLO_ROUND_BASLAT = 0
		gameInfo.DUELLO_ROUND_ZAMAN_IN = 0
		gameInfo.DUELLO_ROUND_ZAMAN_KALAN = 0
		gameInfo.DUELLO_ROUND_DURUM = 0
		gameInfo.DUELLO_SKOR_MY = 0
		gameInfo.DUELLO_SKOR_TARGET = 0
		gameInfo.DUELLO_DURUM = 0
		gameInfo.DUELLO_VID = 0
		gameInfo.DUELLO_BASLATAN = 0
		gameInfo.DUELLO_RAKIP_PARA = 0
		gameInfo.DUELLO_BENIM_PARA = 0
		gameInfo.DUELLO_KABUL = 0
		gameInfo.DUELLO_KABUL_RAKIP = 0
		if "#"+str(gameInfo.DUELLO_RAKIP)+"#" in gameInfo.DUELLO_YOLLAYANLAR:
			gameInfo.DUELLO_YOLLAYANLAR.remove("#"+str(gameInfo.DUELLO_RAKIP)+"#")
		
		if "#"+str(gameInfo.DUELLO_RAKIP)+"#" in gameInfo.DUELLO_YOLLANANLAR:
			gameInfo.DUELLO_YOLLANANLAR.remove("#"+str(gameInfo.DUELLO_RAKIP)+"#")

		gameInfo.DUELLO_RAKIP = ""
		gameInfo.DUELLO_KAPAT = 0

		self.kapat = 0
		self.ItemSlotList = {}
		self.ItemSlotList_Ekipman = {}
		self.ItemSlotList_R = {} ## Rakibin Item Listesi ##
		self.ItemSlotList_R_Ekipman = {} ## Rakibin Ekipman Item Listesi ##
		self.ItemSlotList_R_I = {}
		self.ItemSlotList_R_I_Ekipman = {}
		self.ItemSlot = []
		self.ItemSlot_Ekipman = []

		DUELLO_START = 0
		SEND_START = 0
		ItemSlot_Benim = []
		ItemSlot_Benim2 = []
		ItemSlot_R_Ekle = ""
		ItemSlot_R_Ekle_Ekipman = ""
		ItemSlot = []
		ItemEkle_DURUM = 0
		ItemEkle_DURUM_Ekipman = 0

		self.Hide()

	def __LoadWindow(self):
		global ItemSlot
		try:			
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/iteminewsdialog.py")
		except:
			import exception
			exception.Abort("ItemineDuelloWindow.LoadWindow.LoadObject")
			
		self.wndSlot = self.GetChild("ItemSlot") ## Benim 5x6 ~ 30 Tane Item Slot Ekraným ##
		self.wndSlot_R = self.GetChild("ItemSlot_Rakip") ## Rakibin 5x6 ~ 30 Tane Item Slot Ekraný ##
		self.wndEquip = self.GetChild("equipslot") ## Benim Ekipman Item Slot Ekraný ##
		self.wndEquip_R = self.GetChild("equipslot_r") ## Rakibin Ekipman Item Slot Ekraný ##

		#self.wndEquip = self.GetChild("equipslot")
		self.kabulet_button = self.GetChild("kabulet_button")
		self.iptal_button = self.GetChild("iptal_button")

		self.TitleBar = self.GetChild("TitleBar")		
		self.TitleName = self.GetChild("TitleName")
		
		self.senin_Para = self.GetChild("Money_Slot")
		self.senin_Para_Text = self.GetChild("Money")
		self.rakip_Para_Text = self.GetChild("Money_Rakip")
		self.round_text = self.GetChild("Round_Text")
		self.round_value = self.GetChild("Round_Sayisi")
		self.round_okbutton = self.GetChild("Round_Ok_Button")
		self.round_okbutton.SetEvent(ui.__mem_func__(self.roundDEGISTIR))
		self.roundWindow=Duello_SkorTabelasi()
		self.roundWindow.Hide()

		self.kabuletti_benim = self.GetChild("kabuletti_benim")
		self.kabuletti_rakip = self.GetChild("kabuletti_rakip")
		self.kabuletti_benim.Hide()
		self.kabuletti_rakip.Hide()
		
		if gameInfo.DUELLO_BASLATAN==1:
			self.round_text.Hide()
			self.round_value.Show()
			self.round_okbutton.Show()
		else:
			self.round_text.Show()
			self.round_value.Hide()
			self.round_okbutton.Hide()

		self.wndSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		##self.wndSlot.SAFE_SetButtonEvent("RIGHT", "EXIST", self.UnselectItemSlot)
		self.wndSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.wndSlot.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))

		#self.wndEkipmanSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectItemSlot_Ekipman))

		self.wndSlot_R.SetOverInItemEvent(ui.__mem_func__(self.OverInItem_R))
		self.wndSlot_R.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))

		self.TitleBar.SetCloseEvent(ui.__mem_func__(self.Close2))
		self.wndEquip.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectItemSlot))
		self.wndEquip.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		self.wndEquip.SetOverInItemEvent(ui.__mem_func__(self.OverInItem_Ekipman))
		self.wndEquip.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
		self.wndEquip_R.SetOverInItemEvent(ui.__mem_func__(self.OverInItem_R_Ekipman))
		self.wndEquip_R.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
		self.kabulet_button.SetEvent(ui.__mem_func__(self.__kabulet_button))
		self.iptal_button.SetEvent(ui.__mem_func__(self.Close),1)

		self.senin_Para.SetEvent(ui.__mem_func__(self.__para_button))

		self.LoadData()

	def __para_button(self):
		if gameInfo.DUELLO_KABUL == 0 and gameInfo.DUELLO_KABUL_RAKIP == 0:
			gameInfo.MONEY_INPUT = 2
			self.dlgPickMoney.SetTitleName('Miktar gir')
			self.dlgPickMoney.SetAcceptText('Koy')
			self.dlgPickMoney.Open(player.GetElk())
			self.dlgPickMoney.SetMax(11)
			self.dlgPickMoney.Show()
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "<Düello> : Düello'ya hazýrken bu iþlem yapýlamaz.")

	def __kabulet_button(self):
		net.SendWhisperPacket(gameInfo.DUELLO_RAKIP, "#xsbyfatihbab34ndsawgqwqdhsabdsabdsabwbqdsnandsadnasndas#")
		gameInfo.PYTHONISLEM = "duello_kabul_ediyorum#"+str(gameInfo.DUELLO_RAKIP)
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		self.kabuletti_benim.Show()
		self.kabulet_button.Down()
		gameInfo.DUELLO_KABUL = 1

	def __clear_button(self):
		pass				
					
	def	LoadData(self):
		pass

	def SelectEmptySlot(self, selectedSlotPos):
		global ItemSlot
		global ItemSlot_Benim
		global ItemSlot_Benim2
		global Item_Slot_Eklenen
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			if player.IsEquipmentSlot(attachedSlotPos) and gameInfo.DUELLO_UST==1:
				return

			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				if attachedSlotPos in self.ItemSlot:
					mouseModule.mouseController.DeattachObject()
				else:
				
					if gameInfo.DUELLO_KABUL == 0 and gameInfo.DUELLO_KABUL_RAKIP == 0:
						pass
					else:
						chat.AppendChat(chat.CHAT_TYPE_INFO, "<Düello> : Düello'ya hazýrken bu iþlem yapýlamaz.")
						mouseModule.mouseController.DeattachObject()
						return
				
					itemVnum2 = player.GetItemIndex(attachedSlotPos) 
					item.SelectItem(itemVnum2)
					
					if item.IsAntiFlag(item.ANTIFLAG_GIVE):
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANNOT_GIVE)
						mouseModule.mouseController.DeattachObject()
						return
				
					if int(player.GetItemCount(int(attachedSlotPos))) == 1:
						self.wndSlot.SetItemSlot(int(selectedSlotPos), int(player.GetItemIndex(int(attachedSlotPos))), 0)
					else:
						self.wndSlot.SetItemSlot(int(selectedSlotPos), int(player.GetItemIndex(int(attachedSlotPos))), int(player.GetItemCount(int(attachedSlotPos))))
					self.ItemSlotList["slot"+str(selectedSlotPos)] = attachedSlotPos
					self.ItemSlot.append(attachedSlotPos)
					ItemSlot.append(attachedSlotPos)

					Item_Slot_Eklenen = str(attachedSlotPos)+"#"+str(gameInfo.DUELLO_RAKIP)+"#"+str(selectedSlotPos)
					gameInfo.PYTHONISLEM = "duello_itemekle_slot#"+str(attachedSlotPos)+"#"+str(gameInfo.DUELLO_RAKIP)+"#"+str(selectedSlotPos)
					event.QuestButtonClick(gameInfo.PYTHONTOLUA)

					## Itemi koyduðu zaman rakibe koyduðu itemi belirtme ##
					slotIndex = attachedSlotPos

					itemVnum = player.GetItemIndex(slotIndex)
					itemCount = player.GetItemCount(slotIndex)
					
					metin = ""
					attr = ""

					metinSlot = [player.GetItemMetinSocket(slotIndex, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
					attrSlot = [player.GetItemAttribute(slotIndex, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

					#net.SendWhisperPacket(gameInfo.DUELLO_RAKIP, "#xsbyfatihbab34dsaxaw22121a123q#"+str(selectedSlotPos)+"#"+str(attachedSlotPos)+"#"+str(itemVnum)+"#"+str(itemCount)+"#"+str(metinSlot)+"#"+str(attrSlot)+"#")


		mouseModule.mouseController.DeattachObject()

	def __SetSlot(self, arg):
		self.saveName = "lib/"+str(player.GetName())+str(arg)+".ddr"
		self.LoadData()

	def OverInItem(self, slotNumber):
		#if self.tooltipItem:
		#	self.tooltipItem.SetInventoryItem(int(self.tokens[slotNumber-1]))
		self.tooltipItem.ClearToolTip()
		if "slot"+str(slotNumber) in self.ItemSlotList.keys():
			slotIndex = self.ItemSlotList["slot"+str(slotNumber)]
			#slotIndex = self.ItemSlot

			itemVnum = player.GetItemIndex(slotIndex)
			itemCount = player.GetItemCount(slotIndex)
			
			metinSlot = [player.GetItemMetinSocket(slotIndex, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
			attrSlot = [player.GetItemAttribute(slotIndex, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(metinSlot))
			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(attrSlot))

			self.tooltipItem.AddRefineItemData(itemVnum, metinSlot, attrSlot)

	def OverInItem_R(self, slotNumber):
		self.tooltipItem.ClearToolTip()
		if "slot"+str(slotNumber) in self.ItemSlotList_R.keys():
			slotIndex = self.ItemSlotList_R_I["slot"+str(slotNumber)].split("#")
			#item_adet = self.ItemSlotList_R_I["slot"+str(slotNumber)].split("#")[3].count("@")
			#item_adet2 = self.ItemSlotList_R_I["slot"+str(slotNumber)].split("#")[4].count("@")
			#items = self.ItemSlotList_R_I["slot"+str(slotNumber)].split("#")[3].split("@")
			#items2 = self.ItemSlotList_R_I["slot"+str(slotNumber)].split("#")[4].split("@")

			#metinList = {}
			#metinList["metin"] = list(eval(slotIndex[3]))
				
			#attrList = {}
			#attrList["attr"] = list(eval(slotIndex[4]))
			
			itemVnum = player.GetItemIndex(int(slotIndex[1]))
			itemCount = player.GetItemCount(int(slotIndex[2]))

			items = self.ItemSlotList_R_I["slot"+str(slotNumber)].split("#")

			metinAttr = [int(items[4]),int(items[5]),int(items[6]),int(items[7]),int(items[8]),int(items[9])]
			slotAttr =  [(int(items[10]),int(items[11])),(int(items[12]),int(items[13])),(int(items[14]),int(items[15])),(int(items[16]),int(items[17])),(int(items[18]),int(items[19])),(int(items[20]),int(items[21])),(int(items[22]),int(items[23]))]
	
			self.tooltipItem.AddRefineItemData(int(slotIndex[1]), metinAttr, slotAttr)
			
			#metinSlot = [slotIndex[3].split("|")[i] for i in xrange(player.METIN_SOCKET_MAX_NUM)]
			#attrSlot = [slotIndex[4].split("|")[i] for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

			#mtn = [items[1],items[2],items[3],items[4],items[5],items[6]]
			#attr = [items2[1],items2[2],items2[3],items2[4],items2[5],items2[6],items2[7],items2[8],items2[9],items2[10],items2[11],items2[12],items2[13],items2[14]]

			#metinSlot = [items[i] for i in xrange(item_adet)]
			#attrSlot = [items2[i] for i in xrange(item_adet2)]

			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(slotIndex[3]))
			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(slotIndex[4]))

			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(metinSlot))
			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(attrSlot))
			
			#self.tooltipItem.AddRefineItemData(int(itemVnum), metinSlot, attrSlot)
			#self.tooltipItem.AddRefineItemData(int(itemVnum), metinSlot, attrSlot)

			###self.tooltipItem.AddRefineItemData(int(slotIndex[1]), metinList["metin"], attrList["attr"])

	def OverInItem_Ekipman(self, slotNumber):
		#if self.tooltipItem:
		#	self.tooltipItem.SetInventoryItem(int(self.tokens[slotNumber-1]))
		self.tooltipItem.ClearToolTip()
		#if slotNumber-1 in self.ItemSlotList_Ekipman.keys():
		if "slot_"+str(slotNumber) in self.ItemSlotList_Ekipman.keys():
			slotIndex = self.ItemSlotList_Ekipman["slot_"+str(slotNumber)]
			self.tooltipItem.SetInventoryItem(int(slotIndex))

	def OverInItem_R_Ekipman(self, slotNumber):
		self.tooltipItem.ClearToolTip()
		#if slotNumber-1 in self.ItemSlotList_Ekipman.keys():
		if "slot_"+str(slotNumber) in self.ItemSlotList_R_Ekipman.keys():
			#slotIndex = self.ItemSlotList_R_Ekipman["slot_"+str(slotNumber)].split("#")
			slotIndex = self.ItemSlotList_R_I_Ekipman["slot_"+str(slotNumber)].split("#")

			#metinList = {}
			#metinList["metin"] = list(eval(slotIndex[3]))
				
			#attrList = {}
			#attrList["attr"] = list(eval(slotIndex[4]))
			
			itemVnum = player.GetItemIndex(int(slotIndex[1]))
			itemCount = player.GetItemCount(int(slotIndex[2]))

			items = self.ItemSlotList_R_I_Ekipman["slot_"+str(slotNumber)].split("#")

			metinAttr = [int(items[4]),int(items[5]),int(items[6]),int(items[7]),int(items[8]),int(items[9])]
			slotAttr =  [(int(items[10]),int(items[11])),(int(items[12]),int(items[13])),(int(items[14]),int(items[15])),(int(items[16]),int(items[17])),(int(items[18]),int(items[19])),(int(items[20]),int(items[21])),(int(items[22]),int(items[23]))]
	
			self.tooltipItem.AddRefineItemData(int(slotIndex[1]), metinAttr, slotAttr)
			
			#self.tooltipItem.AddRefineItemData(int(slotIndex[1]), metinList["metin"], attrList["attr"])

	def OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
			
	def roundDEGISTIR(self):
		roundSAYISI=self.round_value.GetText()
		if int(roundSAYISI)==gameInfo.DUELLO_ROUND:
			return
			
		if gameInfo.DUELLO_KABUL == 0 and gameInfo.DUELLO_KABUL_RAKIP == 0:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "<Düello> : Düello'ya hazýrken bu iþlem yapýlamaz.")
			self.round_value.SetText(str(gameInfo.DUELLO_ROUND))
			return
		
		gameInfo.DUELLO_ROUND=int(roundSAYISI)
		gameInfo.PYTHONISLEM="duello_round#"+str(roundSAYISI)+"#"+str(gameInfo.DUELLO_RAKIP)+"#0"
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		net.SendWhisperPacket(gameInfo.DUELLO_RAKIP, "#xsbyfatihbab34dsaxxsadsajdsajroundxsd122121dcxsa#"+str(roundSAYISI))
			
	def SelectItemSlot(self, itemSlotIndex):
		global ItemSlot
		global Item_Equip_Eklenen
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			#slotIndex = self.ItemSlotList_Ekipman[itemSlotIndex-1].split("#")
		
			#itemVnum = player.GetItemIndex(int(slotIndex[1]))
			#itemCount = player.GetItemCount(int(slotIndex[2]))

			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()

			if player.IsEquipmentSlot(attachedSlotPos) and gameInfo.DUELLO_UST==1:
				return

			if itemSlotIndex in self.ItemSlot_Ekipman or attachedSlotPos in self.ItemSlot:
				pass
			else:
			
				if gameInfo.DUELLO_KABUL == 0 and gameInfo.DUELLO_KABUL_RAKIP == 0:
					pass
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "<Düello> : Düello'ya hazýrken bu iþlem yapýlamaz.")
					mouseModule.mouseController.DeattachObject()
					return

				itemIndex = player.GetItemIndex(attachedSlotPos)
				itemCount = player.GetItemCount(attachedSlotPos)
				item.SelectItem(itemIndex)
				
				if item.IsAntiFlag(item.ANTIFLAG_GIVE):
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANNOT_GIVE)
					mouseModule.mouseController.DeattachObject()
					return
				
				itemType = item.GetItemType()
				itemSubType = item.GetItemSubType()

				if itemSlotIndex == 1 and item.IsWearableFlag(item.WEARABLE_BODY):	
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos
				elif itemSlotIndex == 2 and item.IsWearableFlag(item.WEARABLE_HEAD):	
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos
				elif itemSlotIndex == 3 and item.IsWearableFlag(item.WEARABLE_FOOTS):	
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos
				elif itemSlotIndex == 4 and item.IsWearableFlag(item.WEARABLE_WRIST):	
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos
				elif itemSlotIndex == 5 and item.IsWearableFlag(item.WEARABLE_WEAPON):	
					#self.ItemSlotList_Ekipman[int(itemSlotIndex)-1] = attachedSlotPos	
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos	
				elif itemSlotIndex == 6 and item.IsWearableFlag(item.WEARABLE_NECK):		
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos	
				elif itemSlotIndex == 7 and item.IsWearableFlag(item.WEARABLE_EAR):	
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos
				elif itemSlotIndex == 8 and item.IsWearableFlag(item.WEARABLE_SHIELD):	
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos
				else:		
					return

				Item_Equip_Eklenen = str(attachedSlotPos)+"#"+str(gameInfo.DUELLO_RAKIP)+"#"+str(itemSlotIndex)
				gameInfo.PYTHONISLEM = "duello_itemekle_equip#"+str(attachedSlotPos)+"#"+str(gameInfo.DUELLO_RAKIP)+"#"+str(itemSlotIndex)
				event.QuestButtonClick(gameInfo.PYTHONTOLUA)
			
				self.ItemSlot_Ekipman.append(itemSlotIndex)
				self.ItemSlot.append(attachedSlotPos)
				ItemSlot.append(attachedSlotPos)

				if itemCount == 1:
					self.wndEquip.SetItemSlot(int(itemSlotIndex), int(itemIndex), 0)
				else:
					self.wndEquip.SetItemSlot(int(itemSlotIndex), int(itemIndex), int(itemCount))

				metinSlot = [player.GetItemMetinSocket(attachedSlotPos, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
				attrSlot = [player.GetItemAttribute(attachedSlotPos, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

				#net.SendWhisperPacket(gameInfo.DUELLO_RAKIP, "#xsbyfatihbab34dsaxaw2x2121a123q#"+str(itemSlotIndex)+"#"+str(attachedSlotPos)+"#"+str(itemIndex)+"#"+str(itemCount)+"#"+str(metinSlot)+"#"+str(attrSlot)+"#")
					
				#open(self.saveName, "w").write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % tuple(self.tokens))	
					
				mouseModule.mouseController.DeattachObject()
		
	def OnUpdate(self):
		global ItemEkle_DURUM
		global ItemEkle_DURUM_Ekipman
		global ItemSlot_R_Ekle
		global ItemSlot_R_Ekle_Ekipman
		global DUELLO_START
		global SEND_START

		self.TitleName.SetText(str(gameInfo.DUELLO_RAKIP) + " adlý oyuncuyla eþyalý düello panelin.")
		self.senin_Para_Text.SetText(str(localeInfo.NumberToMoneyString(gameInfo.DUELLO_BENIM_PARA)))
		self.rakip_Para_Text.SetText(str(localeInfo.NumberToMoneyString(gameInfo.DUELLO_RAKIP_PARA)))
		self.round_text.SetText(str(gameInfo.DUELLO_ROUND))

		if gameInfo.DUELLO_DURUM==1:
			self.roundWindow.Show()
		else:
			self.roundWindow.Hide()
			
		if int(gameInfo.DUELLO_RAKIP_PARA) != 0:
			if int(gameInfo.DUELLO_RAKIP_PARA)+int(self.param) >= 1999999999:
				self.Close()
		
		if gameInfo.DUELLO_KABUL_RAKIP == 1:
			self.kabuletti_rakip.Show()
			if gameInfo.DUELLO_KABUL == 1:
				if gameInfo.DUELLO_BASLATAN == 2 and DUELLO_START == 0:
					net.SendChatPacket("/pvp %d" % (int(gameInfo.DUELLO_VID)))
					DUELLO_START = 1
				if SEND_START == 0:
					gameInfo.DUELLO_DURUM = 1
					SEND_START = 1

		if gameInfo.DUELLO_KABUL_RAKIP == 1 and gameInfo.DUELLO_KABUL == 1:
			gameInfo.DUELLO_DURUM = 1
			self.SetPosition(9000, 5000)

		if gameInfo.DUELLO_KABUL == 1:
			self.kabulet_button.Down()
			
		if player.IsOpenPrivateShop():
			self.Close()

		#if gameInfo.DUELLO_RAKIP == "":
		if gameInfo.DUELLO_KAPAT == 1:
			self.kapat = 1
			self.roundWindow.Hide()
			self.Close()

		if ItemEkle_DURUM == 1:
			bol = ItemSlot_R_Ekle.split("#")
			#self.ItemSlotList_R["slot"+str(bol[1])] = int(bol[2])
			self.ItemSlotList_R["slot"+str(bol[26])] = int(bol[3])
			#self.ItemSlotList_R_I["slot"+str(bol[1])] = "#"+str(bol[3])+"#"+str(bol[4])+"#"+str(bol[5])+"#"+str(bol[6])+"#"
			self.ItemSlotList_R_I["slot"+str(bol[26])] = ItemSlot_R_Ekle
			if int(bol[2]) == 1:
				self.wndSlot_R.SetItemSlot(int(bol[26]), int(bol[1]), 0)
			else:
				self.wndSlot_R.SetItemSlot(int(bol[26]), int(bol[1]), int(bol[2]))
			ItemEkle_DURUM = 0
			##self.ItemSlot_R.append(attachedSlotPos)

		if ItemEkle_DURUM_Ekipman == 1:
			bol = ItemSlot_R_Ekle_Ekipman.split("#")
			#self.ItemSlotList_R_Ekipman["slot_"+str(bol[1])] = int(bol[2])
			self.ItemSlotList_R_Ekipman["slot_"+str(bol[26])] = int(bol[3])
			#self.ItemSlotList_R_I_Ekipman["slot_"+str(bol[1])] = "#"+str(bol[3])+"#"+str(bol[4])+"#"+str(bol[5])+"#"+str(bol[6])+"#"
			self.ItemSlotList_R_I_Ekipman["slot_"+str(bol[26])] = ItemSlot_R_Ekle_Ekipman
			if int(bol[2]) == 1:
				self.wndEquip_R.SetItemSlot(int(bol[26]), int(bol[1]), 0)
			else:
				self.wndEquip_R.SetItemSlot(int(bol[26]), int(bol[1]), int(bol[2]))
			ItemEkle_DURUM_Ekipman = 0
					
	def OnPressEscapeKey(self):
		#import interfaceModule
		#self.interface = interfaceModule.Interface()
		#self.interface.OpenSystemDialog()
		return TRUE
		
	def OnPressExitKey(self):
		#import interfaceModule
		#self.interface = interfaceModule.Interface()
		#self.interface.OpenSystemDialog()
		return TRUE
		
class Duello_SkorTabelasi(ui.Board):

	def __init__(self):
		ui.Board.__init__(self)
		
		self.Config()

	def __del__(self):
		ui.Board.__del__(self)
		
	def Config(self):
		self.SetSize(210, 54)
		self.SetPosition(3,42)
		y=8
		y2=18
		self.roundHAZIR_T=0
		self.roundHAZIR_ISLEM=0
		self.isimSENIN = ui.TextLine()
		self.isimSENIN.SetParent(self)
		self.isimSENIN.SetDefaultFontName()
		self.isimSENIN.SetPosition(-112+21, -y)
		self.isimSENIN.SetText(str(player.GetName()) + " :")
		self.isimSENIN.SetWindowVerticalAlignCenter()
		self.isimSENIN.SetWindowHorizontalAlignCenter()
		self.isimSENIN.Show()	
		
		self.skorSENIN = ui.TextLine()
		self.skorSENIN.SetParent(self)
		self.skorSENIN.SetFontName("Tahoma:22")
		self.skorSENIN.SetPosition(-18+1, -y2)
		self.skorSENIN.SetText("2 -")
		self.skorSENIN.SetWindowVerticalAlignCenter()
		self.skorSENIN.SetWindowHorizontalAlignCenter()
		self.skorSENIN.Show()	
		
		self.isimRAKIP = ui.TextLine()
		self.isimRAKIP.SetParent(self)
		self.isimRAKIP.SetDefaultFontName()
		self.isimRAKIP.SetPosition(125-76-15, -y)
		#self.isimRAKIP.SetText(": " + str(gameInfo.DUELLO_RAKIP))
		self.isimRAKIP.SetText(": HasskTR")
		self.isimRAKIP.SetWindowVerticalAlignCenter()
		self.isimRAKIP.SetWindowHorizontalAlignCenter()
		self.isimRAKIP.Show()
		
		self.skorRAKIP = ui.TextLine()
		self.skorRAKIP.SetParent(self)
		self.skorRAKIP.SetFontName("Tahoma:22")
		self.skorRAKIP.SetPosition(12+1, -y2)
		self.skorRAKIP.SetText("1")
		self.skorRAKIP.SetWindowVerticalAlignCenter()
		self.skorRAKIP.SetWindowHorizontalAlignCenter()
		self.skorRAKIP.Show()
		
		self.roundSAYISI = ui.TextLine()
		self.roundSAYISI.SetParent(self)
		self.roundSAYISI.SetDefaultFontName()
		self.roundSAYISI.SetPosition(-17,10)
		self.roundSAYISI.SetText("fatihbab34, 2015.9.21 <3")
		self.roundSAYISI.SetWindowVerticalAlignCenter()
		self.roundSAYISI.SetWindowHorizontalAlignCenter()
		self.roundSAYISI.Show()
		
		self.roundHAZIR = ui.TextLine()
		self.roundHAZIR.SetParent(self)
		self.roundHAZIR.SetDefaultFontName()
		self.roundHAZIR.SetPosition(-36,26)
		self.roundHAZIR.SetText("fatihbab34, 2015.9.21 <3")
		self.roundHAZIR.SetWindowVerticalAlignCenter()
		self.roundHAZIR.SetWindowHorizontalAlignCenter()
		self.roundHAZIR.Hide()
		
		self.roundHazirBUTTON = self.Button(self, 'Hazýr', '', 71, 78, self.__roundHAZIR, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.roundHazirBUTTON.Hide()
		
	def __roundHAZIR(self):
		if int(player.GetStatus(player.HP)) <= 0:
			return
		gameInfo.DUELLO_ROUND_HAZIR_MY=1
		net.SendWhisperPacket(gameInfo.DUELLO_RAKIP, "#xsbyfatihbab34dasddjsadjsajmwmwqroundhazirndsandsad#")
		
	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetEvent(func)
		return button
		
	def OnUpdate(self):
		self.isimRAKIP.SetText(": " + str(gameInfo.DUELLO_RAKIP))
		self.skorSENIN.SetText(str(gameInfo.DUELLO_SKOR_MY) + " -")
		self.skorRAKIP.SetText(str(gameInfo.DUELLO_SKOR_TARGET))
		#self.roundSAYISI.SetText("Kalan Round : " + str(8-(gameInfo.DUELLO_SKOR_MY+gameInfo.DUELLO_SKOR_TARGET)))
		self.roundSAYISI.SetText("Bitiþ : " + str(gameInfo.DUELLO_ROUND))
		
		if gameInfo.DUELLO_ROUND_HAZIR_TARGET==0:
			self.roundHAZIR.SetText("Rakip : " + "|cFFFF0000|H|hHazýr deðil.")
		else:
			self.roundHAZIR.SetText("Rakip : " + "|cFF32CD32|H|hHazýr!")
			
		if gameInfo.DUELLO_ROUND_HAZIR_MY==1 and gameInfo.DUELLO_ROUND_HAZIR_TARGET==1:
			if player.IsRevengeInstance(gameInfo.DUELLO_VID):
				net.SendChatPacket("/pvp %d" % (int(gameInfo.DUELLO_VID)))
			gameInfo.DUELLO_ROUND_HAZIR_MY=0
			gameInfo.DUELLO_ROUND_HAZIR_TARGET=0
			self.roundHAZIR_ISLEM=0

		if self.roundHAZIR_T==0 and gameInfo.DUELLO_ROUND_HAZIR_MY==0:
			self.roundHazirBUTTON.SetUp()
			self.roundHazirBUTTON.Enable()
			self.roundHAZIR_T=1
			
		if gameInfo.DUELLO_ROUND_YENILE==1:
			self.roundHAZIR_T=0
			self.roundHAZIR_ISLEM=1
			gameInfo.DUELLO_ROUND_YENILE=0
			
		if self.roundHAZIR_ISLEM==1:
			self.SetSize(210,54+54)
			self.roundHAZIR.Show()
			self.roundHazirBUTTON.Show()
		else:
			self.SetSize(210,54)
			self.roundHAZIR.Hide()
			self.roundHazirBUTTON.Hide()
		
		if gameInfo.DUELLO_ROUND_HAZIR_MY == 1:
			self.roundHazirBUTTON.Down()
			self.roundHazirBUTTON.Disable()
		
class Duello_para_ayarlari(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.unitValue = 1
		self.maxValue = 0
		self.eventAccept = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/PickMoneyDialog.py")
		except:
			import exception
			exception.Abort("MoneyDialog.LoadDialog.LoadScript")

		try:
			self.board = self.GetChild("board")
			self.maxValueTextLine = self.GetChild("max_value")
			self.pickValueEditLine = self.GetChild("money_value")
			self.acceptButton = self.GetChild("accept_button")
			self.cancelButton = self.GetChild("cancel_button")
		except:
			import exception
			exception.Abort("MoneyDialog.LoadDialog.BindObject")

		self.pickValueEditLine.SetReturnEvent(ui.__mem_func__(self.OnAlisveris))
		self.pickValueEditLine.SetEscapeEvent(ui.__mem_func__(self.Close))
		self.acceptButton.SetEvent(ui.__mem_func__(self.OnAlisveris))
		self.cancelButton.SetEvent(ui.__mem_func__(self.Close))
		self.board.SetCloseEvent(ui.__mem_func__(self.Close))

	def Destroy(self):
		self.ClearDictionary()
		self.eventAccept = 0
		self.maxValue = 0
		self.pickValueEditLine = 0		
		self.acceptButton = 0
		self.cancelButton = 0
		self.board = None

	def SetTitleName(self, text):
		self.board.SetTitleName(text)

	def SetAcceptText(self, gelen):
		self.acceptButton.SetText(str(gelen))
		
	def SetAcceptEvent(self, event):
		self.eventAccept = event

	def SetMax(self, max):
		self.pickValueEditLine.SetMax(max)

	def Open(self, maxValue, unitValue=1):

		if localeInfo.IsYMIR() or localeInfo.IsCHEONMA() or localeInfo.IsHONGKONG():
			unitValue = ""

		width = self.GetWidth()
		(mouseX, mouseY) = wndMgr.GetMousePosition()

		if mouseX + width/2 > wndMgr.GetScreenWidth():
			xPos = wndMgr.GetScreenWidth() - width
		elif mouseX - width/2 < 0:
			xPos = 0
		else:
			xPos = mouseX - width/2

		self.SetPosition(xPos, mouseY - self.GetHeight() - 20)

		if localeInfo.IsARABIC():
			self.maxValueTextLine.SetText("/" + str(maxValue))
		else:
			self.maxValueTextLine.SetText(" / " + str(maxValue))

		self.pickValueEditLine.SetText(str(unitValue))
		self.pickValueEditLine.SetFocus()

		ime.SetCursorPosition(1)

		self.unitValue = unitValue
		self.maxValue = maxValue
		self.Show()
		self.SetTop()

	def Close(self):
		self.pickValueEditLine.KillFocus()
		gameInfo.MONEY_INPUT = 0
		self.Hide()

	def OnAlisveris(self):

		text = self.pickValueEditLine.GetText()

		if len(text) > 0 and text.isdigit():

			money = int(text)
			money = min(money, self.maxValue)

			if money > 0:
				if self.eventAccept:
					self.eventAccept(money)

			if player.GetElk() < int(text):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.DUELLO_PARA_YOK)
				return

			#net.SendWhisperPacket(gameInfo.DUELLO_RAKIP, "#xsbyfatihbab34sdajdsamdasdnsawnwqwusdadxasmdasdasxasbndadasnas#"+str(text)+"#")
				
			gameInfo.DUELLO_BENIM_PARA = int(text)
			gameInfo.PYTHONISLEM = "duello_para_ekle#"+str(text)+"#"+str(gameInfo.DUELLO_RAKIP)+"#"
			event.QuestButtonClick(gameInfo.PYTHONTOLUA)


		self.Close()

class Bug_Fatihbab34(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

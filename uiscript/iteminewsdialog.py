import uiScriptLocale
import item
import gameInfo

window = {
	"name" : "ItemineDuelloWindow",

	"x" : SCREEN_WIDTH - 360 - 220 - 180,
	"y" : SCREEN_HEIGHT - 37 - 565 - 30,

	"style" : ("movable", "float",),

	"width" : 413-6,
	"height" : 474+50,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 413-6,
			"height" : 474+50,
			
			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 6,

					"width" : 394,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":80+90+60-10-8-1, "y":3, "text":"Ýtemine Duello Paneli", "text_horizontal_align":"center" },
					),
				},

				## Equipment Slot
				{
					"name" : "equip_Base",
					"type" : "image",

					"x" : 13+31-11,
					"y" : 9+25,
					
					"image" : "d:/ymir work/ui/game/windows/equipment_base.sub",
				},		

				{
					"name" : "equipslot_r",
					"type" : "slot",
					"x" : 16+31-11,
					"y" : 12+25,

					"width" : 130,
					"height" : 150,

					"slot" : (
								{"index":1, "x":39, "y":37, "width":32, "height":64},
								{"index":2, "x":39, "y":2, "width":32, "height":32},
								{"index":3, "x":39, "y":145-5, "width":32, "height":32},
								{"index":4, "x":75, "y":67, "width":32, "height":32},
								{"index":5, "x":3, "y":3, "width":32, "height":96},
								{"index":6, "x":116, "y":84, "width":32, "height":32},
								{"index":7, "x":116, "y":52, "width":32, "height":32},
								{"index":8, "x":75, "y":35, "width":32, "height":32},
							),
				},
				
				
				{
					"name" : "equip_Base_2",
					"type" : "image",

					"x" : 195+31-11,
					"y" : 9+25,
					
					"image" : "d:/ymir work/ui/game/windows/equipment_base.sub",
				},		

				{
					"name" : "equipslot",
					"type" : "slot",
					"x" : 195+31-11,
					"y" : 12+25,

					"width" : 130,
					"height" : 150,

					"slot" : (
								{"index":1, "x":39, "y":37, "width":32, "height":64},
								{"index":2, "x":39, "y":2, "width":32, "height":32},
								{"index":3, "x":39, "y":145-5, "width":32, "height":32},
								{"index":4, "x":75, "y":67, "width":32, "height":32},
								{"index":5, "x":3, "y":3, "width":32, "height":96},
								{"index":6, "x":116, "y":84, "width":32, "height":32},
								{"index":7, "x":116, "y":52, "width":32, "height":32},
								{"index":8, "x":75, "y":35, "width":32, "height":32},
							),
				},
				
				#ek itemler(rakip)
				
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 211+2,
					"y" : 270-30-10,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 6,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub"
				},
				
				#benim
				
				{
					"name" : "ItemSlot_Rakip",
					"type" : "grid_table",


					"x" : 9+6+15,
					"y" : 270-30-10,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 6,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub"
				},
				
				#para yeri(rakip)
				
				{
					"name":"Money_Slot_Rakip",
					"type":"button",

					"x":-30-60,
 
                    "y":28+24-20+40+8,

					"horizontal_align":"center",
					"vertical_align":"bottom",

					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

					"children" :
					(
						{
							"name":"Money_Icon_Rakip",
							"type":"image",

							"x":-18,
							"y":2,

							"image":"d:/ymir work/ui/game/windows/money_icon.sub",
						},

						{
							"name" : "Money_Rakip",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "0 Yang",
						},
					),
				},
				
				#para yeri (benim)
				{
					"name":"Money_Slot",
					"type":"button",

					"x":8+90,
 
                    "y":28+24-20+40+8,

					"horizontal_align":"center",
					"vertical_align":"bottom",

					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

					"children" :
					(
						{
							"name":"Money_Icon",
							"type":"image",

							"x":-18,
							"y":2,

							"image":"d:/ymir work/ui/game/windows/money_icon.sub",
						},

						{
							"name" : "Money",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "0 Yang",
						},
					),
				},

				## Round(Disable)
				{"name":"Round_Title","type":"text","x":-2,"y":480-9,"text":"Round :","horizontal_align":"center","text_horizontal_align":"center"},
				{
					"name" : "Round_SlotBar",
					"type" : "slotbar",
					"x" : 8-13,
					"y" : 480-6+14,

					"horizontal_align":"center",
					
					"width" : 28,
					"height" : 18,

					"children" :
					(
						{
							"name":"Round_Icon",
							"type":"image",

							"x":-18+9000,
							"y":2,

							"image":"d:/ymir work/ui/game/windows/money_icon.sub",
						},

						{
							"name" : "Round_Text",
							"type" : "text",

							"x" : 0,
							"y" : 3,

							"horizontal_align" : "center",
							"text_horizontal_align" : "center",

							"text" : "1",
						},
						
						{
							"name" : "Round_Sayisi",
							"type" : "editline",
							
							"width" : 26,
							"height" : 48,
							
							"text"	: "1",
							
							"input_limit" : 1,
							
							"x" : 2,
							"y" : 2,
						
						},
					),
				},

				{
					"name" : "Round_Ok_Button",
					"type" : "button",
					
					"x" : 407/2+100-41-40,
					"y" : 480-6+14,
					
					"text" : "ok",
					
					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
				},


				## Benim Kabul Etti Icon

				
				{
					"name" : "kabuletti_benim",
					"type" : "ani_image",

					#"x" : 245-17,
					#"y" : 250,
					
					"x" : 251-37,
					"y" : 271-38,
					
					"images" : (
						#gameInfo.CONFIG_YOL+"accept.tga",
						gameInfo.CONFIG_YOL+"kabul2.tga",
					),
				},

				{
					"name" : "kabuletti_rakip",
					"type" : "ani_image",

					#"x" : 72-21,
					#"y" : 250,
					
					"x" : 29,
					"y" : 271-38,
					
					"images" : (
						#gameInfo.CONFIG_YOL+"accept.tga",
						gameInfo.CONFIG_YOL+"kabul2.tga",
					),
				},

				{
					"name" : "kabulet_button",
					"type" : "button",

					"x" : 45+260,
					"y" : 235+189-25+29 + 95 - 30 - 30+10,

					"text" : "Hazýr",
					"tooltip_text" : "Düello'ya baþlamak için kabul et!",

					"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",
				},
				{
					"name" : "iptal_button",
					"type" : "button",

					"x" : 45+260,
					"y" : 265+189-25-9+29 + 95 - 30 - 30 + 10,
					
					#"x" : 320,
					#"y" : 181,

					"text" : "iptal",

					"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",
				},
				{
					"name" : "eq0",
					"type" : "button",

					"x" : 50+9000,
					"y" : 295,

					"text" : "1",

					"default_image" : "d:/ymir work/ui/public/minimize_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/minimize_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/minimize_button_03.sub",
				},				
				{
					"name" : "eq1",
					"type" : "button",

					"x" : 65+9000,
					"y" : 295,

					"text" : "2",

					"default_image" : "d:/ymir work/ui/public/minimize_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/minimize_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/minimize_button_03.sub",
				},				
				{
					"name" : "eq2",
					"type" : "button",

					"x" : 80+9000,
					"y" : 295,

					"text" : "3",

					"default_image" : "d:/ymir work/ui/public/minimize_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/minimize_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/minimize_button_03.sub",
				},				
				{
					"name" : "eq3",
					"type" : "button",

					"x" : 95+9000,
					"y" : 295,

					"text" : "4",

					"default_image" : "d:/ymir work/ui/public/minimize_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/minimize_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/minimize_button_03.sub",
				},				
				{
					"name" : "eq4",
					"type" : "button",

					"x" : 110+9000,
					"y" : 295,

					"text" : "5",

					"default_image" : "d:/ymir work/ui/public/minimize_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/minimize_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/minimize_button_03.sub",
				},
			),
		},
	),
}
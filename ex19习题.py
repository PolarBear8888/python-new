def pens_and_boxes(count_pens, boxes):
    print(f"I have {count_pens} pens!")
    print(f"I have {boxes} boxes now!")

print('ONE')
  
count_pens = 10
boxes = 10
pens_and_boxes(count_pens, boxes)

print('TWO')
pens = 11
pencil_boxes = 11
pens_and_boxes(pens, pencil_boxes)

print('Three')
pens_and_boxes(12,12)

print("Four")
count_pens= input()
boxes = input()
pens_and_boxes(count_pens,boxes)

print('Five')
count_pens = 3* (input())
boxes = 3*(input())
pens_and_boxes(count_pens,boxes)

print("Six")
count_pens = 10
pens_and_boxes(count_pens,pencil_boxes + 10)

print("Seven")
pens_and_boxes(pens + 10 ,pencil_boxes + 10)




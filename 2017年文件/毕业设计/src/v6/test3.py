# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 09:32:02 2016

@author: http://blog.csdn.net/lql0716
"""

#首先确定目标区域的矩形框坐标，只需左上角的点和右下角的点的坐标，即mouseStart和mouseEnd，前一帧img1，当前帧img2
def histMatch(mouseStart, mouseEnd, img1, img2):  #对相邻两帧的某个目标做直方图跟踪匹配， 仅仅是匹配目标的大致区域,传入的图片为彩色

    a1 = mouseStart[1]  #矩形区域左侧边 x坐标
    a2 = mouseEnd[1]    #矩形区域右侧边 x坐标
    b1 = mouseStart[0]  #矩形区域上侧边 y坐标
    b2 = mouseEnd[0]    #矩形区域下侧边 y坐标
    height = mouseEnd[1] - mouseStart[1]
    weight = mouseEnd[0] - mouseStart[0]
    ratio = np.float(weight) / np.float(height)  #weight与height的比例
#    mask = np.zeros(img.shape[:2],np.uint8)  #掩码操作，只对指定区域操作，这里初始值为 0，指定区域为 1

    histsize = 256

    #opencv方法读取-cv2.calcHist（速度最快）, 图像，通道[0]-灰度图，掩码-无，灰度级，像素范围
    hist_full = cv2.calcHist([img1[a1:a2,b1:b2]],[0],None,[histsize],[0,256])

    min = np.array([0.0, 0.0, 0.0, 0.0])

    search_1 = 10  #搜索范围
    search_2 = 0

    if search_2 > 0:
        #移动矩形区域左上角的点坐标，同时改变长和宽，进行搜索相似度最高的直方图
        for i in range(-search_1, search_1+1):
            for j in range(-search_1, search_1+1):
                for k in range(-search_2, search_2+1):
                    if i == -search_1 and j == -search_1 and k == -search_2:
                        x1 = a1 + i
                        x2 = x1 + (height + k)   #调整height的长度
                        y1 = b1 + j
                        y2 = y1 + (weight + int(round(k*ratio)))   #调整weight的长度      
                    else:
                        x1 = a1 + i
                        x2 = x1 + (height + k)    #调整height的长度
                        y1 = b1 + j
                        y2 = y1 + (weight + int(round(k*ratio)))   #调整weight的长度

                    hist_full2 = cv2.calcHist([img2[x1:x2, y1:y2]],[0],None,[histsize],[0,256])
                    comp = cv2.compareHist(hist_full, hist_full2, cv2.cv.CV_COMP_BHATTACHARYYA)
        #            print comp
                    if i == -search_1 and j == -search_1 and k == -search_2:
                        min[0]=comp
                        min[1]=i*1.0
                        min[2]=j*1.0
                        min[3]=k*1.0
        #                print 'a'
                    else:
                        if comp < min[0]:
                            min[0]=comp 
                            min[1]=i*1.0
                            min[2]=j*1.0
                            min[3]=k*1.0
        #                    print 'b'
                        else:
                            continue

                    #cv2.HISTCMP_BHATTACHARYYA  测试集测试，效果最好
                    #cv2.HISTCMP_CHISQR
                    #cv2.HISTCMP_CHISQR_ALT    效果第三
                    #cv2.HISTCMP_CORREL     效果很差
                    #cv2.HISTCMP_HELLINGER   效果第二
                    #cv2.HISTCMP_INTERSECT   效果很差
                    #cv2.HISTCMP_KL_DIV    效果很差

    #                cv2.cv.CV_COMP_BHATTACHARYYA  效果较好
    #                cv2.cv.CV_COMP_CHISQR   效果很差
    #                cv2.cv.CV_COMP_CORREL   效果比第一个稍差
    #                cv2.cv.CV_COMP_INTERSECT   效果很差
            #        print comp
        print min
        a = int(min[1])  #矩形左上角点的x坐标
        b = int(min[2])  #矩形左上角点的y坐标
        c = int(min[3])  #height的增量

        new_a1 = a1 + a
        new_a2 = new_a1 + (height + c)
        new_b1 = b1 + b
        new_b2 = b1 + (weight + int(round(c*ratio)))

        new_h = height + c
        new_w = weight + int(round(c*ratio))

    #    cv2.rectangle(img2,(new_b1,new_a1),(new_b2,new_a2),(0,0,255),1,8)  #画矩形函数cv2.rectangle

        new_mouse_start = np.array([new_b1, new_a1])
        new_mouse_end = np.array([new_b2, new_a2])

        return new_mouse_start, new_mouse_end

    else:
        #移动矩形区域左上角的点坐标，进行搜索相似度最高的直方图
        for i in range(-search_1, search_1+1):
            for j in range(-search_1, search_1+1):

                if i == -search_1 and j == -search_1:
                    x1 = a1 + i
                    x2 = x1 + height   
                    y1 = b1 + j
                    y2 = y1 + weight      
                else:
                    x1 = a1 + i
                    x2 = x1 + height   
                    y1 = b1 + j
                    y2 = y1 + weight                         

                hist_full2 = cv2.calcHist([img2[x1:x2, y1:y2]],[0],None,[histsize],[0,256])
                comp = cv2.compareHist(hist_full, hist_full2, cv2.cv.CV_COMP_BHATTACHARYYA)
                if i == -search_1 and j == -search_1:
                    min[0]=comp
                    min[1]=i*1.0
                    min[2]=j*1.0
#                    min[3]=k*1.0
    #                print 'a'
                else:                
                    if comp < min[0]:
                        min[0]=comp 
                        min[1]=i*1.0
                        min[2]=j*1.0
#                        min[3]=k*1.0
    #                    print 'b'
                    else:
                        continue

                    #cv2.HISTCMP_BHATTACHARYYA  测试集测试，效果最好
                    #cv2.HISTCMP_CHISQR
                    #cv2.HISTCMP_CHISQR_ALT    效果第三
                    #cv2.HISTCMP_CORREL     效果很差
                    #cv2.HISTCMP_HELLINGER   效果第二
                    #cv2.HISTCMP_INTERSECT   效果很差
                    #cv2.HISTCMP_KL_DIV    效果很差

    #                cv2.cv.CV_COMP_BHATTACHARYYA  效果较好
    #                cv2.cv.CV_COMP_CHISQR   效果很差
    #                cv2.cv.CV_COMP_CORREL   效果比第一个稍差
    #                cv2.cv.CV_COMP_INTERSECT   效果很差
            #        print comp
        print min
        a = int(min[1])  #矩形左上角点的x坐标
        b = int(min[2])  #矩形左上角点的y坐标

        new_a1 = a1 + a
        new_a2 = new_a1 + height
        new_b1 = b1 + b
        new_b2 = new_b1 + weight

    #    cv2.rectangle(img2,(new_b1,new_a1),(new_b2,new_a2),(0,0,255),1,8)  #画矩形函数cv2.rectangle

        new_mouse_start = np.array([new_b1, new_a1])
        new_mouse_end = np.array([new_b2, new_a2])

        return new_mouse_start, new_mouse_end

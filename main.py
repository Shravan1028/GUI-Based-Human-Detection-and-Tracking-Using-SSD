
# GUI-Based Real-Time Human Detection and Tracking Using SSD and Haar-Cascade Classifier.

import argparse
import threading
import tkinter as tk
import tkinter.messagebox as mbox
import warnings
# imported necessary library
from tkinter import *
from tkinter import filedialog

import cv2
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
from fpdf import FPDF

from persondetection import DetectorAPI

import warnings

# Main Window & Configuration
window = tk.Tk()
window.title("GUI-Based Real-Time Human Detection and Tracking Using SSD and Haar-Cascade Classifier")
window.iconbitmap('Images/icon.ico')
window.geometry('1000x700')
window.configure(bg='#011119')



gif_frames = []
frames_delay = 0


def ready_gif():
    global frames_delay
    # print("started")
    gif_file = Image.open("Images/main-gif.gif")
    # print(gif_file.n_frames)

    for r in range (0, gif_file.n_frames):
        gif_file.seek(r)
        gif_frames.append(gif_file.copy())
        # print(gif_file.copy())

    frames_delay = gif_file.info['duration']
    # print("comp")
    play_gif()

frame_count = -1

def play_gif():
    global frame_count, current_frame

    if frame_count >= len(gif_frames) - 1:
        frame_count = -1
        play_gif()
    else:
        frame_count += 1
        current_frame =ImageTk.PhotoImage(gif_frames[frame_count])
        gif_lb.config(image=current_frame)
    # print("play")
    window.after(frames_delay, play_gif)

gif_lb = tk.Label(window)
gif_lb.pack()
gif_lb.place(x=320, y=240)

threading.Thread(target=ready_gif).start()



# top label
start1 = tk.Label(text = "GUI-Based REAL-TIME\nHUMAN DETECTION  &  TRACKING", font=("Times New Roman", 40,"underline"), fg="white", bg = "#011119") # same way bg
start1.place(x = 60, y = 70)

start2 = tk.Label(text = "Guided By : Prof. Radha Shirbhate \nMade by: Dhaval Pawar, Shravan Singh, Shivam Randive", font=("Helvetica", 10), fg="gray", bg = "#011119") # same way bg
start2.place(x = 360, y = 655)

# function defined to start the main application
def start_fun():
    window.destroy()

# created a start button
Button(window, text="▶ START",command=start_fun,font=("Google Sans", 25), bg = "#FB2576", fg = "white", cursor="hand2", borderwidth=3, relief="raised").place(x = 70 , y =420 )

# # image on the main window
# path1 = "Images/front2.png"
# img2 = ImageTk.PhotoImage(Image.open(path1))
# panel1 = tk.Label(window, image = img2)
# panel1.place(x = 90, y = 250)

# # image on the main window
# path = "Images/front1.png"
# img1 = ImageTk.PhotoImage(Image.open(path))
# panel = tk.Label(window, image = img1)
# panel.place(x = 380, y = 180)

exit1 = False
# function created for exiting from window
def exit_win():
    global exit1
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        exit1 = True
        window.destroy()

# exit button created
Button(window, text="❌ EXIT",command=exit_win,font=("Google Sans", 25), bg = "red", fg = "white", cursor="hand2", borderwidth=3, relief="raised").place(x =790 , y = 420 )

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

if exit1==False:
    # Main Window & Configuration of window1
    window1 = tk.Tk()
    window1.title("GUI-Based Real-Time Human Detection and Tracking Using SSD and Haar-Cascade Classifier")
    window1.iconbitmap('Images/icon.ico')
    window1.geometry('1000x700')
    window1.configure(bg='#011119')

    filename=""
    filename1=""
    filename2=""

    def argsParser():
        arg_parse = argparse.ArgumentParser()
        arg_parse.add_argument("-v", "--video", default=None, help="path to Video File ")
        arg_parse.add_argument("-i", "--image", default=None, help="path to Image File ")
        arg_parse.add_argument("-c", "--camera", default=False, help="Set true if you want to use the camera.")
        arg_parse.add_argument("-o", "--output", type=str, help="path to optional output video file")
        args = vars(arg_parse.parse_args())
        return args

    # ---------------------------- image section ------------------------------------------------------------
    def image_option():
        # new windowi created for image section
        windowi = tk.Tk()
        windowi.title("Human Detection from Image")
        windowi.iconbitmap('Images/icon.ico')
        windowi.geometry('1000x700')
        windowi.configure(bg='#011119')

        max_count1 = 0
        framex1 = []
        county1 = []
        max1 = []
        avg_acc1_list = []
        max_avg_acc1_list = []
        max_acc1 = 0
        max_avg_acc1 = 0

        # function defined to open the image
        def open_img():
            global filename1, max_count1, framex1, county1, max1, avg_acc1_list, max_avg_acc1_list, max_acc1, max_avg_acc1
            max_count1 = 0
            framex1 = []
            county1 = []
            max1 = []
            avg_acc1_list = []
            max_avg_acc1_list = []
            max_acc1 = 0
            max_avg_acc1 = 0

            filename1 = filedialog.askopenfilename(title="Select Image file", parent = windowi)
            path_text1.delete("1.0", "end")
            path_text1.insert(END, filename1)

        # function defined to detect the image
        def det_img():
            global filename1, max_count1, framex1, county1, max1, avg_acc1_list, max_avg_acc1_list, max_acc1, max_avg_acc1
            max_count1 = 0
            framex1 = []
            county1 = []
            max1 = []
            avg_acc1_list = []
            max_avg_acc1_list = []
            max_acc1 = 0
            max_avg_acc1 = 0

            image_path = filename1
            if(image_path==""):
                mbox.showerror("Error", "No Image File Selected!", parent = windowi)
                return
            info1.config(text="Status : Detecting...")
            # info2.config(text="                                                  ")
            mbox.showinfo("Status", "Detecting, Please Wait...", parent = windowi)
            # time.sleep(1)
            detectByPathImage(image_path)

        # main detection process process here
        def detectByPathImage(path):
            global filename1, max_count1, framex1, county1, max1, avg_acc1_list, max_avg_acc1_list, max_acc1, max_avg_acc1
            max_count1 = 0
            framex1 = []
            county1 = []
            max1 = []
            avg_acc1_list = []
            max_avg_acc1_list = []
            max_acc1 = 0
            max_avg_acc1 = 0

            # function defined to plot the enumeration fo people detected
            def img_enumeration_plot():
                windowi.title("Plot for Image")  # Set the window title

                fig = plt.figure(facecolor='#008B8B')
                ax = plt.axes()
                ax.set_facecolor("#00ecec")
                plt.plot(framex1, county1, label="Human Count", color="green", marker='o', markerfacecolor='blue')
                plt.plot(framex1, max1, label="Max. Human Count", linestyle='dashed', color='fuchsia')
                plt.xlabel('Time (sec)')
                plt.ylabel('Human Count')
                plt.legend()
                plt.title("Enumeration Plot")
                plt.legend()
                plt.show()

                # Embed the matplotlib plot into the Tkinter window
                #canvas = FigureCanvasTkAgg(fig, master=windowi)
                #canvas_widget = canvas.get_tk_widget()
                #canvas_widget.pack()

                # Close the Matplotlib figure
                plt.close(fig)


            def img_accuracy_plot():
                plt.figure(facecolor='#008B8B')
                ax = plt.axes()
                ax.set_facecolor("#00ecec")
                plt.plot(framex1, avg_acc1_list, label="Avg. Accuracy", color="green", marker='o', markerfacecolor='blue')
                plt.plot(framex1, max_avg_acc1_list, label="Max. Avg. Accuracy", linestyle='dashed', color='fuchsia')
                plt.xlabel('Time (sec)')
                plt.ylabel('Avg. Accuracy')
                plt.title('Plot for Image')  # Set the title using plt.title
                plt.legend()
                plt.show()


            def img_gen_report():
                pdf = FPDF(orientation='P', unit='mm', format='A4')
                pdf.add_page()
                pdf.set_font("Helvetica", "", 20)
                pdf.set_text_color(128, 0, 0)
                pdf.image('Images/Crowd_Report.png', x=0, y=0, w=210, h=297)

                pdf.text(125, 150, str(max_count1))
                pdf.text(105, 163, str(max_acc1))
                pdf.text(125, 175, str(max_avg_acc1))
                if (max_count1 > 25):
                    pdf.text(26, 220, "Max. Human Detected is greater than MAX LIMIT.")
                    pdf.text(70, 235, "Region is Crowded.")
                else:
                    pdf.text(26, 220, "Max. Human Detected is in range of MAX LIMIT.")
                    pdf.text(65, 235, "Region is not Crowded.")

                pdf.output('Crowd_Report.pdf')
                mbox.showinfo("Status", "Report Generated and Saved Successfully.", parent = windowi)


            odapi = DetectorAPI()
            threshold = 0.7

            image = cv2.imread(path)
            img = cv2.resize(image, (image.shape[1], image.shape[0]))
            boxes, scores, classes, num = odapi.processFrame(img)
            person = 0
            acc=0
            for i in range(len(boxes)):

                if classes[i] == 1 and scores[i] > threshold:
                    box = boxes[i]
                    person += 1
                    cv2.rectangle(img, (box[1], box[0]), (box[3], box[2]), (255,0,0), 2)  # cv2.FILLED #BGR
                    cv2.putText(img, f'P{person, round(scores[i], 2)}', (box[1] - 30, box[0] - 8), cv2.FONT_HERSHEY_COMPLEX,0.5, (0, 0, 255), 1)  # (75,0,130),
                    acc += scores[i]
                    if (scores[i] > max_acc1):
                        max_acc1 = scores[i]

            if (person > max_count1):
                max_count1 = person
            if(person>=1):
                if((acc / person) > max_avg_acc1):
                    max_avg_acc1 = (acc / person)


            cv2.imshow("Human Detection from Image", img)
            info1.config(text="                                                  ")
            info1.config(text="Status : Detection & Counting Completed")
            # info2.config(text="                                                  ")
            # info2.config(text="Max. Human Count : " + str(max_count1))
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            for i in range(20):
                framex1.append(i)
                county1.append(max_count1)
                max1.append(max_count1)
                avg_acc1_list.append(max_avg_acc1)
                max_avg_acc1_list.append(max_avg_acc1)

            Button(windowi, text="Enumeration\nPlot", command=img_enumeration_plot, cursor="hand2", font=("Helvetica", 20),bg="#FF34B3", fg="#10FCFD").place(x=100, y=530)
            Button(windowi, text="Avg. Accuracy\nPlot", command=img_accuracy_plot, cursor="hand2", font=("Helvetica", 20),bg="#FF34B3", fg="#10FCFD").place(x=700, y=530)
            Button(windowi, text="Generate  Crowd  Report", command=img_gen_report, cursor="hand2", font=("Helvetica", 20),bg="#FF34B3", fg="#10FCFD").place(x=325, y=550)

        def prev_img():
            global filename1
            img = cv2.imread(filename1, 1)
            cv2.imshow("Selected Image Preview", img)

        # for images ----------------------
        lbl1 = tk.Label(windowi,text="DETECT  FROM\nIMAGE", font=("Times New Roman", 50, "underline"),fg="white", bg = "#011119")
        lbl1.place(x=230, y=20)
        lbl2 = tk.Label(windowi,text="Selected Image", font=("Helvetica", 30), fg="#10FCFD",bg="#FF34B3")
        lbl2.place(x=80, y=200)
        lbl3 = tk.Label(windowi,text = "Guided By : Prof. Radha Shirbhate \nMade by: Dhaval Pawar, Shravan Singh, Shivam Randive", font=("Helvetica", 10), fg="gray", bg = "#011119") # same way bg
        lbl3.place(x = 360, y = 655)
        path_text1 = tk.Text(windowi, height=1, width=37, font=("Helvetica", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
        path_text1.place(x=80, y = 260)

        Button(windowi, text="SELECT", command=open_img, cursor="hand2", font=("Google Sans", 20), bg="#FF34B3", fg="#10FCFD").place(x=220, y=350)
        Button(windowi, text="PREVIEW",command=prev_img, cursor="hand2", font=("Google Sans", 20), bg = "#FF34B3", fg = "#10FCFD").place(x = 410, y = 350)
        Button(windowi, text="DETECT",command=det_img, cursor="hand2", font=("Google Sans", 20), bg = "#FF34B3", fg = "#10FCFD").place(x = 620, y = 350)

        info1 = tk.Label(windowi,font=( "Helvetica", 30),fg="#011119",bg="#011119")
        info1.place(x=100, y=445)
        # info2 = tk.Label(windowi,font=("Helvetica", 30), fg="gray")
        # info2.place(x=100, y=500)

        def exit_wini():
            if mbox.askokcancel("Exit", "Do you want to exit?", parent = windowi):
                windowi.destroy()
        windowi.protocol("WM_DELETE_WINDOW", exit_wini)


    # ---------------------------- video section ------------------------------------------------------------
    def video_option():
        # new windowv created for video section
        windowv = tk.Tk()
        windowv.title("Human Detection from Video")
        windowv.iconbitmap('Images/icon.ico')
        windowv.geometry('1000x700')
        windowv.configure(bg='#011119')
        max_count2 = 0
        framex2 = []
        county2 = []
        max2 = []
        avg_acc2_list = []
        max_avg_acc2_list = []
        max_acc2 = 0
        max_avg_acc2 = 0

        # function defined to open the video
        def open_vid():
            global filename2, max_count2, framex2, county2, max2, avg_acc2_list, max_avg_acc2_list, max_acc2, max_avg_acc2
            max_count2 = 0
            framex2 = []
            county2 = []
            max2=[]
            avg_acc2_list = []
            max_avg_acc2_list = []
            max_acc2 = 0
            max_avg_acc2 = 0

            filename2 = filedialog.askopenfilename(title="Select Video file", parent=windowv)
            path_text2.delete("1.0", "end")
            path_text2.insert(END, filename2)

        # function defined to detect inside the video
        def det_vid():
            global filename2, max_count2, framex2, county2, max2, avg_acc2_list, max_avg_acc2_list, max_acc2, max_avg_acc2
            max_count2 = 0
            framex2 = []
            county2 = []
            max2 = []
            avg_acc2_list = []
            max_avg_acc2_list = []
            max_acc2 = 0
            max_avg_acc2 = 0

            video_path = filename2
            if (video_path == ""):
                mbox.showerror("Error", "No Video File Selected!", parent = windowv)
                return
            info1.config(text="Status : Detecting...")
            # info2.config(text="                                                  ")
            mbox.showinfo("Status", "Detecting, Please Wait...", parent=windowv)
            # time.sleep(1)

            args = argsParser()
            writer = None
            if args['output'] is not None:
                writer = cv2.VideoWriter(args['output'], cv2.VideoWriter_fourcc(*'MJPG'), 10, (600, 600))

            detectByPathVideo(video_path, writer)

        # the main process of detection in video takes place here
        def detectByPathVideo(path, writer):
            global filename2, max_count2, framex2, county2, max2, avg_acc2_list, max_avg_acc2_list, max_acc2, max_avg_acc2
            max_count2 = 0
            framex2 = []
            county2 = []
            max2 = []
            avg_acc2_list = []
            max_avg_acc2_list = []
            max_acc2 = 0
            max_avg_acc2 = 0

            # function defined to plot the people detected in video
            def vid_enumeration_plot():
                plt.figure(facecolor='#008B8B', )
                ax = plt.axes()
                ax.set_facecolor("#00ecec")
                plt.plot(framex2, county2, label = "Human Count", color = "green", marker='o', markerfacecolor='blue')
                plt.plot(framex2, max2, label="Max. Human Count", linestyle='dashed', color='fuchsia')
                plt.xlabel('Time (sec)')
                plt.ylabel('Human Count')
                plt.title('Enumeration Plot')
                plt.legend()
                #plt.get_current_fig_manager().canvas.set_window_title("Plot for Video")
                plt.show()

            def vid_accuracy_plot():
                plt.figure(facecolor='#008B8B', )
                ax = plt.axes()
                ax.set_facecolor("#00ecec")
                plt.plot(framex2, avg_acc2_list, label="Avg. Accuracy", color="green", marker='o', markerfacecolor='blue')
                plt.plot(framex2, max_avg_acc2_list, label="Max. Avg. Accuracy", linestyle='dashed', color='fuchsia')
                plt.xlabel('Time (sec)')
                plt.ylabel('Avg. Accuracy')
                plt.title('Avg. Accuracy Plot')
                plt.legend()
                #plt.get_current_fig_manager().canvas.set_window_title("Plot for Video")
                plt.show()

            def vid_gen_report():
                pdf = FPDF(orientation='P', unit='mm', format='A4')
                pdf.add_page()
                pdf.set_font("Arial", "", 20)
                pdf.set_text_color(128, 0, 0)
                pdf.image('Images/Crowd_Report.png', x=0, y=0, w=210, h=297)

                pdf.text(125, 150, str(max_count2))
                pdf.text(105, 163, str(max_acc2))
                pdf.text(125, 175, str(max_avg_acc2))
                if(max_count2>25):
                    pdf.text(26, 220, "Max. Human Detected is greater than MAX LIMIT.")
                    pdf.text(70, 235, "Region is Crowded.")
                else:
                    pdf.text(26, 220, "Max. Human Detected is in range of MAX LIMIT.")
                    pdf.text(65, 235, "Region is not Crowded.")

                pdf.output('Crowd_Report.pdf')
                mbox.showinfo("Status", "Report Generated and Saved Successfully.", parent = windowv)

            video = cv2.VideoCapture(path)
            odapi = DetectorAPI()
            threshold = 0.7

            check, frame = video.read()
            if check == False:
                print('Video Not Found. Please Enter a Valid Path (Full path of Video Should be Provided).')
                return

            x2 = 0
            while video.isOpened():
                # check is True if reading was successful
                check, frame = video.read()
                if(check==True):
                    img = cv2.resize(frame, (800, 500))
                    boxes, scores, classes, num = odapi.processFrame(img)
                    person = 0
                    acc = 0
                    for i in range(len(boxes)):
                        # print(boxes)
                        # print(scores)
                        # print(classes)
                        # print(num)
                        # print()
                        if classes[i] == 1 and scores[i] > threshold:
                            box = boxes[i]
                            person += 1
                            cv2.rectangle(img, (box[1], box[0]), (box[3], box[2]), (255, 0, 0), 2)  # cv2.FILLED
                            cv2.putText(img, f'P{person, round(scores[i],2)}', (box[1]-30, box[0]-8), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 1 )#(75,0,130),
                            acc+=scores[i]
                            if(scores[i]>max_acc2):
                                max_acc2 = scores[i]

                    if(person>max_count2):
                        max_count2 = person
                    county2.append(person)
                    x2+=1
                    framex2.append(x2)
                    if(person>=1):
                        avg_acc2_list.append(acc/person)
                        if((acc/person)>max_avg_acc2):
                            max_avg_acc2 = (acc/person)
                    else:
                        avg_acc2_list.append(acc)

                    if writer is not None:
                        writer.write(img)

                    cv2.imshow("Human Detection from Video", img)
                    key = cv2.waitKey(1)
                    if key & 0xFF == ord('q'):
                        break
                else:
                    break

            video.release()
            info1.config(text="                                                  ")
            # info2.config(text="                                                  ")
            info1.config(text="Status : Detection & Counting Completed")
            # info2.config(text="Max. Human Count : " + str(max_count2))
            cv2.destroyAllWindows()

            for i in range(len(framex2)):
                max2.append(max_count2)
                max_avg_acc2_list.append(max_avg_acc2)

            Button(windowv, text="Enumeration\nPlot", command=vid_enumeration_plot, cursor="hand2", font=("Google Sans", 20),bg="#FF34B3", fg="#10FCFD").place(x=100, y=530)
            Button(windowv, text="Avg. Accuracy\nPlot", command=vid_accuracy_plot, cursor="hand2", font=("Google Sans", 20),bg="#FF34B3", fg="#10FCFD").place(x=700, y=530)
            Button(windowv, text="Generate  Crowd  Report", command=vid_gen_report, cursor="hand2", font=("Google Sans", 20),bg="#FF34B3", fg="#10FCFD").place(x=325, y=550)

        # funcion defined to preview the selected video
        def prev_vid():
            global filename2
            cap = cv2.VideoCapture(filename2)
            while (cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                    img = cv2.resize(frame, (800, 500))
                    cv2.imshow('Selected Video Preview', img)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            cv2.destroyAllWindows()


        lbl1 = tk.Label(windowv, text="DETECT  FROM\nVIDEO", font=("Times New Roman", 50, "underline"), fg="white", bg = "#011119")
        lbl1.place(x=230, y=20)
        lbl2 = tk.Label(windowv, text="Selected Video", font=("Helvetica", 30), fg="#10FCFD",bg="#FF34B3")
        lbl2.place(x=80, y=200)
        lbl3 = tk.Label(windowv,text = "Guided By : Prof. Radha Shirbhate \nMade by: Dhaval Pawar, Shravan Singh, Shivam Randive", font=("Helvetica", 10), fg="gray", bg = "#011119") # same way bg
        lbl3.place(x = 360, y = 655)
        path_text2 = tk.Text(windowv, height=1, width=37, font=("Helvetica", 30), bg="light yellow", fg="orange", borderwidth=2,relief="solid")
        path_text2.place(x=80, y=260)

        Button(windowv, text="SELECT", command=open_vid, cursor="hand2", font=("Arial", 20), bg="#FF34B3", fg="#10FCFD").place(x=220, y=350)
        Button(windowv, text="PREVIEW", command=prev_vid, cursor="hand2", font=("Arial", 20), bg="#FF34B3", fg="#10FCFD").place(x=410, y=350)
        Button(windowv, text="DETECT", command=det_vid, cursor="hand2", font=("Arial", 20), bg="#FF34B3", fg="#10FCFD").place(x=620, y=350)

        info1 = tk.Label(windowv, font=("Arial", 30), fg="#011119",bg="#011119")  # same way bg
        info1.place(x=100, y=440)
        # info2 = tk.Label(windowv, font=("Arial", 30), fg="gray")  # same way bg
        # info2.place(x=100, y=500)

        #function defined to exit from windowv section
        def exit_winv():
            if mbox.askokcancel("Exit", "Do you want to exit?", parent = windowv):
                windowv.destroy()
        windowv.protocol("WM_DELETE_WINDOW", exit_winv)


    # ---------------------------- camera section ------------------------------------------------------------
    def camera_option():
        # new window created for camera section
        windowc = tk.Tk()
        windowc.title("Human Detection from Camera")
        windowc.iconbitmap('Images/icon.ico')
        windowc.geometry('1000x700')
        windowc.configure(bg='#011119')

        max_count3 = 0
        framex3 = []
        county3 = []
        max3 = []
        avg_acc3_list = []
        max_avg_acc3_list = []
        max_acc3 = 0
        max_avg_acc3 = 0

        # function defined to open the camera
        def open_cam():
            global max_count3, framex3, county3, max3, avg_acc3_list, max_avg_acc3_list, max_acc3, max_avg_acc3
            max_count3 = 0
            framex3 = []
            county3 = []
            max3 = []
            avg_acc3_list = []
            max_avg_acc3_list = []
            max_acc3 = 0
            max_avg_acc3 = 0

            args = argsParser()

            info1.config(text="Status : Opening Camera...")
            # info2.config(text="                                                  ")
            mbox.showinfo("Status", "Opening Camera...Please Wait...", parent=windowc)
            # time.sleep(1)

            writer = None
            if args['output'] is not None:
                writer = cv2.VideoWriter(args['output'], cv2.VideoWriter_fourcc(*'MJPG'), 10, (600, 600))
            if True:
                detectByCamera(writer)

        # function defined to detect from camera
        def detectByCamera(writer):
            global max_count3, framex3, county3, max3, avg_acc3_list, max_avg_acc3_list, max_acc3, max_avg_acc3
            max_count3 = 0
            framex3 = []
            county3 = []
            max3 = []
            avg_acc3_list = []
            max_avg_acc3_list = []
            max_acc3 = 0
            max_avg_acc3 = 0

            # function defined to plot the people count in camera
            def cam_enumeration_plot():
                plt.figure(facecolor='#008B8B', )
                ax = plt.axes()
                ax.set_facecolor("#00ecec")
                plt.plot(framex3, county3, label="Human Count", color="green", marker='o', markerfacecolor='blue')
                plt.plot(framex3, max3, label="Max. Human Count", linestyle='dashed', color='fuchsia')
                plt.xlabel('Time (sec)')
                plt.ylabel('Human Count')
                plt.legend()
                plt.title("Enumeration Plot")
                #plt.get_current_fig_manager().canvas.set_window_title("Plot for Camera")
                plt.show()

            def cam_accuracy_plot():
                plt.figure(facecolor='#008B8B', )
                ax = plt.axes()
                ax.set_facecolor("#00ecec")
                plt.plot(framex3, avg_acc3_list, label="Avg. Accuracy", color="green", marker='o', markerfacecolor='blue')
                plt.plot(framex3, max_avg_acc3_list, label="Max. Avg. Accuracy", linestyle='dashed', color='fuchsia')
                plt.xlabel('Time (sec)')
                plt.ylabel('Avg. Accuracy')
                plt.title('Avg. Accuracy Plot')
                plt.legend()
                #plt.get_current_fig_manager().canvas.set_window_title("Plot for Camera")
                plt.show()

            def cam_gen_report():
                pdf = FPDF(orientation='P', unit='mm', format='A4')
                pdf.add_page()
                pdf.set_font("Arial", "", 20)
                pdf.set_text_color(128, 0, 0)
                pdf.image('Images/Crowd_Report.png', x=0, y=0, w=210, h=297)

                pdf.text(125, 150, str(max_count3))
                pdf.text(105, 163, str(max_acc3))
                pdf.text(125, 175, str(max_avg_acc3))
                if (max_count3 > 25):
                    pdf.text(26, 220, "Max. Human Detected is greater than MAX LIMIT.")
                    pdf.text(70, 235, "Region is Crowded.")
                else:
                    pdf.text(26, 220, "Max. Human Detected is in range of MAX LIMIT.")
                    pdf.text(65, 235, "Region is not Crowded.")

                pdf.output('Crowd_Report.pdf')
                mbox.showinfo("Status", "Report Generated and Saved Successfully.", parent = windowc)

            video = cv2.VideoCapture(0)
            odapi = DetectorAPI()
            threshold = 0.7

            x3 = 0
            while True:
                check, frame = video.read()
                img = cv2.resize(frame, (800, 600))
                boxes, scores, classes, num = odapi.processFrame(img)
                person = 0
                acc = 0
                for i in range(len(boxes)):

                    if classes[i] == 1 and scores[i] > threshold:
                        box = boxes[i]
                        person += 1
                        cv2.rectangle(img, (box[1], box[0]), (box[3], box[2]), (255, 0, 0), 2)  # cv2.FILLED
                        cv2.putText(img, f'P{person, round(scores[i], 2)}', (box[1] - 30, box[0] - 8),cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)  # (75,0,130),
                        acc += scores[i]
                        if (scores[i] > max_acc3):
                            max_acc3 = scores[i]

                if (person > max_count3):
                    max_count3 = person

                if writer is not None:
                    writer.write(img)

                cv2.imshow("Human Detection from Camera", img)
                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    break

                county3.append(person)
                x3 += 1
                framex3.append(x3)
                if(person>=1):
                    avg_acc3_list.append(acc / person)
                    if ((acc / person) > max_avg_acc3):
                        max_avg_acc3 = (acc / person)
                else:
                    avg_acc3_list.append(acc)

            video.release()
            info1.config(text="                                                  ")
            # info2.config(text="                                                  ")
            info1.config(text="Status : Detection & Counting Completed")
            # info2.config(text="Max. Human Count : " + str(max_count3))
            cv2.destroyAllWindows()

            for i in range(len(framex3)):
                max3.append(max_count3)
                max_avg_acc3_list.append(max_avg_acc3)

            Button(windowc, text="Enumeration\nPlot", command=cam_enumeration_plot, cursor="hand2", font=("Arial", 20),bg="#FF34B3", fg="#10FCFD").place(x=100, y=530)
            Button(windowc, text="Avg. Accuracy\nPlot", command=cam_accuracy_plot, cursor="hand2", font=("Arial", 20),bg="#FF34B3", fg="#10FCFD").place(x=700, y=530)
            Button(windowc, text="Generate  Crowd  Report", command=cam_gen_report, cursor="hand2", font=("Arial", 20),bg="#FF34B3", fg="#10FCFD").place(x=325, y=550)

        lbl1 = tk.Label(windowc, text="DETECT  FROM\nCAMERA", font=("Times New Roman", 50, "underline"), fg="white", bg="#011119")  # same way bg
        lbl1.place(x=230, y=20)
        lbl2 = tk.Label(windowc,text = "Guided By : Prof. Radha Shirbhate \nMade by: Dhaval Pawar, Shravan Singh, Shivam Randive", font=("Helvetica", 10), fg="gray", bg = "#011119") # same way bg
        lbl2.place(x = 360, y = 655)

        Button(windowc, text="OPEN CAMERA", command=open_cam, cursor="hand2", font=("Times New Roman", 20), bg="#FF34B3", fg="#10FCFD").place(x=370, y=230)

        info1 = tk.Label(windowc, font=("Helvetica", 30), fg="#011119",bg="#011119")  # same way bg
        info1.place(x=100, y=330)
        # info2 = tk.Label(windowc, font=("Arial", 30), fg="gray")  # same way bg
        # info2.place(x=100, y=390)

        # function defined to exit from the camera window
        def exit_winc():
            if mbox.askokcancel("Exit", "Do you want to exit?", parent = windowc):
                windowc.destroy()
        windowc.protocol("WM_DELETE_WINDOW", exit_winc)


    # options -----------------------------
    lbl1 = tk.Label(text="DETECT AND ANALYZE FROM ", font=("Times New Roman", 35, "underline"),fg="white", bg='#011119')  # same way bg
    lbl1.place(x=150, y=80)
    
    gbd = tk.Label(text = "Guided By : Prof. Radha Shirbhate \nMade by: Dhaval Pawar, Shravan Singh, Shivam Randive", font=("Helvetica", 10), fg="gray", bg = "#011119")
    gbd.place(x = 360, y = 655)
   

    # image on the main window
    pathi = "Images/img-bg.png"
    imgi = ImageTk.PhotoImage(Image.open(pathi))
    paneli = tk.Label(window1, image = imgi)
    paneli.place(x = 90, y = 210)

    # image on the main window
    pathv = "Images/vid-play.jpg"
    imgv = ImageTk.PhotoImage(Image.open(pathv))
    panelv = tk.Label(window1, image = imgv)
    panelv.place(x = 400, y = 210)# 720, 260

    # image on the main window
    pathc = "Images/download.jpeg"
    imgc = ImageTk.PhotoImage(Image.open(pathc))
    panelc = tk.Label(window1, image = imgc)
    panelc.place(x = 710, y = 210)

    # created button for all three option
    Button(window1, text="IMAGE ➡",command=image_option, cursor="hand2", font=("Arial",20), bg = "#FF34B3", fg = "#10FCFD").place(x = 120, y = 400)
    Button(window1, text="VIDEO ➡",command=video_option, cursor="hand2", font=("Arial", 20), bg = "#EE30A7", fg = "#10FCFD").place(x = 420, y = 400) #90, 300
    Button(window1, text="CAMERA ➡",command=camera_option, cursor="hand2", font=("Arial", 20), bg = "#CD2990", fg = "#10FCFD").place(x = 720, y = 400)

    # function defined to exit from window1
    def exit_win1():
        if mbox.askokcancel("Exit", "Do you want to exit?"):
            window1.destroy()

    # created exit button
    Button(window1, text="❌ EXIT",command=exit_win1,  cursor="hand2", font=("Google Sans", 25), bg = "red", fg = "white").place(x = 420, y = 550)

    window1.protocol("WM_DELETE_WINDOW", exit_win1)
    window1.mainloop()
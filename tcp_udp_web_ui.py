from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout, QVBoxLayout
import sys


class ToolsUi(QDialog):
    # 信号槽机制：设置一个信号，用于触发接收区写入动作
    # 메시지 출력을 위한 Signal and Slot
    signal_write_msg = QtCore.pyqtSignal(str)

    def __init__(self, num):
        """
        初始化窗口
        초기화
        :param num: 计数窗口
        """
        super(ToolsUi, self).__init__()
        self.num = num
        self._translate = QtCore.QCoreApplication.translate

        self.setObjectName("TCP-UDP")
        self.resize(640, 480)
        self.setAcceptDrops(False)
        self.setSizeGripEnabled(False)

        # 定义控件
        # 각 컨트롤 정의
        self.pushButton_get_ip = QtWidgets.QPushButton()
        self.pushButton_link = QtWidgets.QPushButton()
        self.pushButton_unlink = QtWidgets.QPushButton()
        self.pushButton_clear = QtWidgets.QPushButton()
        self.pushButton_exit = QtWidgets.QPushButton()
        self.pushButton_send = QtWidgets.QPushButton()
        self.pushButton_dir = QtWidgets.QPushButton()
        self.pushButton_else = QtWidgets.QPushButton()
        self.label_port = QtWidgets.QLabel()
        self.label_ip = QtWidgets.QLabel()
        self.label_rev = QtWidgets.QLabel()
        self.label_send = QtWidgets.QLabel()
        self.label_sendto = QtWidgets.QLabel()
        self.label_dir = QtWidgets.QLabel()
        self.label_written = QtWidgets.QLabel()
        self.lineEdit_port = QtWidgets.QLineEdit()
        self.lineEdit_ip_send = QtWidgets.QLineEdit()
        self.lineEdit_ip_local = QtWidgets.QLineEdit()
        self.textEdit_send = QtWidgets.QTextEdit()
        self.textBrowser_recv = QtWidgets.QTextBrowser()
        self.comboBox_tcp = QtWidgets.QComboBox()

        self.label_RD = QtWidgets.QLabel()
        self.pushButton_RD_send = QtWidgets.QPushButton()

        self.label_make_csv = QtWidgets.QLabel()
        self.pushButton_make_csv = QtWidgets.QPushButton()

        # 定义布局
        # 레이아웃 정의
        self.h_box_1 = QHBoxLayout()
        self.h_box_2 = QHBoxLayout()
        self.h_box_3 = QHBoxLayout()
        self.h_box_4 = QHBoxLayout()
        self.h_box_5 = QHBoxLayout()
        self.h_box_recv = QHBoxLayout()
        self.h_box_exit = QHBoxLayout()
        self.h_box_all = QHBoxLayout()
        self.v_box_set = QVBoxLayout()
        self.v_box_send = QVBoxLayout()
        self.v_box_web = QVBoxLayout()
        self.v_box_exit = QVBoxLayout()
        self.v_box_right = QVBoxLayout()
        self.v_box_left = QVBoxLayout()

        # 向选择功能的下拉菜单添加选项
        # ComboBox 정의
        self.comboBox_tcp.addItem("")
        self.comboBox_tcp.addItem("")
        self.comboBox_tcp.addItem("")
        self.comboBox_tcp.addItem("")
        self.comboBox_tcp.addItem("")

        # 设置字体
        # 글꼴 설정
        font = QtGui.QFont()
        font.setFamily("Yuppy TC")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_rev.setFont(font)
        self.label_send.setFont(font)

        # 设置控件的初始属性
        # 컨트롤 초기 설정
        self.label_dir.hide()
        self.label_sendto.hide()
        self.pushButton_dir.hide()
        self.lineEdit_ip_send.hide()
        self.label_make_csv.hide()
        self.pushButton_make_csv.hide()
        self.label_dir.setWordWrap(True)  # 让label自动换行
        self.pushButton_unlink.setEnabled(False)
        # self.textBrowser_recv.insertPlainText("这是窗口-%s\n" % self.num)
        self.textBrowser_recv.insertPlainText("다이얼로그-%s\n" % self.num)

        # 调用布局方法和控件显示文字的方法
        # 초기화 함수 호출
        self.layout_ui()
        self.ui_translate()
        self.connect()

    def layout_ui(self):
        """
        设置控件的布局
        레이아웃 설정
        :return:
        """
        # 左侧布局添加
        self.h_box_1.addWidget(self.label_ip)
        self.h_box_1.addWidget(self.lineEdit_ip_local)
        self.h_box_1.addWidget(self.pushButton_get_ip)
        self.h_box_2.addWidget(self.label_port)
        self.h_box_2.addWidget(self.lineEdit_port)
        self.h_box_2.addWidget(self.pushButton_else)
        self.h_box_3.addWidget(self.label_sendto)
        self.h_box_3.addWidget(self.lineEdit_ip_send)
        self.h_box_4.addWidget(self.comboBox_tcp)
        self.h_box_4.addWidget(self.pushButton_link)
        self.h_box_4.addWidget(self.pushButton_unlink)

        self.h_box_5.addWidget(self.label_RD)
        self.h_box_5.addWidget(self.pushButton_RD_send)

        self.h_box_5.addWidget(self.label_make_csv)
        self.h_box_5.addWidget(self.pushButton_make_csv)

        self.v_box_set.addLayout(self.h_box_1)
        self.v_box_set.addLayout(self.h_box_2)
        self.v_box_set.addLayout(self.h_box_3)
        self.v_box_set.addLayout(self.h_box_4)

        self.v_box_set.addLayout(self.h_box_5)

        self.v_box_web.addWidget(self.label_dir)
        self.v_box_web.addWidget(self.pushButton_dir)
        self.v_box_send.addWidget(self.label_send)
        self.v_box_send.addWidget(self.textEdit_send)
        self.v_box_send.addLayout(self.v_box_web)
        self.v_box_exit.addWidget(self.pushButton_send)
        self.v_box_exit.addWidget(self.pushButton_exit)
        self.h_box_exit.addWidget(self.label_written)
        self.h_box_exit.addLayout(self.v_box_exit)
        self.v_box_left.addLayout(self.v_box_set)
        self.v_box_left.addLayout(self.v_box_send)
        self.v_box_left.addLayout(self.h_box_exit)

        # 右侧布局添加
        # 오른쪽 레이아웃 설정
        self.h_box_recv.addWidget(self.label_rev)
        self.h_box_recv.addWidget(self.pushButton_clear)
        self.v_box_right.addLayout(self.h_box_recv)
        self.v_box_right.addWidget(self.textBrowser_recv)

        # 将左右布局添加到窗体布局
        # 오른쪽 왼쪽 레이아웃 설정
        self.h_box_all.addLayout(self.v_box_left)
        self.h_box_all.addLayout(self.v_box_right)

        # 设置窗体布局到窗体
        # 전체 설정
        self.setLayout(self.h_box_all)

    def ui_translate(self):
        """
        控件默认显示文字的设置
        텍스트 정의
        :param : QDialog类创建的对象
        :return: None
        """
        # 设置各个控件显示的文字
        # 也可使用控件的setText()方法设置文字
        # self.setWindowTitle(self._translate("TCP-UDP", "TCP/UDP网络测试工具-窗口%s" % self.num))
        self.setWindowTitle(self._translate("TCP-UDP", "TCP/UDP 테스트 다이얼로그-%s" % self.num))
        # self.comboBox_tcp.setItemText(0, self._translate("TCP-UDP", "TCP服务端"))
        self.comboBox_tcp.setItemText(0, self._translate("TCP-UDP", "TCP Server"))
        # self.comboBox_tcp.setItemText(1, self._translate("TCP-UDP", "TCP客户端"))
        self.comboBox_tcp.setItemText(1, self._translate("TCP-UDP", "TCP Client"))
        # self.comboBox_tcp.setItemText(2, self._translate("TCP-UDP", "UDP服务端"))
        self.comboBox_tcp.setItemText(2, self._translate("TCP-UDP", "UDP Server"))
        # self.comboBox_tcp.setItemText(3, self._translate("TCP-UDP", "UDP客户端"))
        self.comboBox_tcp.setItemText(3, self._translate("TCP-UDP", "UDP Client"))
        # self.comboBox_tcp.setItemText(4, self._translate("TCP-UDP", "WEB服务端"))
        self.comboBox_tcp.setItemText(4, self._translate("TCP-UDP", "WEB Server"))
        # self.pushButton_link.setText(self._translate("TCP-UDP", "连接网络"))
        self.pushButton_link.setText(self._translate("TCP-UDP", "Connect"))
        # self.pushButton_unlink.setText(self._translate("TCP-UDP", "断开网络"))
        self.pushButton_unlink.setText(self._translate("TCP-UDP", "Disconnect"))
        # self.pushButton_get_ip.setText(self._translate("TCP-UDP", "重新获取IP"))
        self.pushButton_get_ip.setText(self._translate("TCP-UDP", "IP 복원"))
        # self.pushButton_clear.setText(self._translate("TCP-UDP", "清除消息"))
        self.pushButton_clear.setText(self._translate("TCP-UDP", "delete msg"))
        # self.pushButton_send.setText(self._translate("TCP-UDP", "发送"))
        self.pushButton_send.setText(self._translate("TCP-UDP", "send msg"))
        # self.pushButton_exit.setText(self._translate("TCP-UDP", "退出系统"))
        self.pushButton_exit.setText(self._translate("TCP-UDP", "system quit"))
        # self.pushButton_dir.setText(self._translate("TCP-UDP", "选择路径"))
        self.pushButton_dir.setText(self._translate("TCP-UDP", "find path"))
        # self.pushButton_else.setText(self._translate("TCP-UDP", "窗口多开another"))
        self.pushButton_else.setText(self._translate("TCP-UDP", "new dlg"))
        # self.label_ip.setText(self._translate("TCP-UDP", "本机IP:"))
        self.label_ip.setText(self._translate("TCP-UDP", "IP:"))
        # self.label_port.setText(self._translate("TCP-UDP", "端口号:"))
        self.label_port.setText(self._translate("TCP-UDP", "Port:"))
        # self.label_sendto.setText(self._translate("TCP-UDP", "目标IP:"))
        self.label_sendto.setText(self._translate("TCP-UDP", "Target IP:"))
        # self.label_rev.setText(self._translate("TCP-UDP", "接收区域"))
        self.label_rev.setText(self._translate("TCP-UDP", "Receive msg"))
        # self.label_send.setText(self._translate("TCP-UDP", "发送区域"))
        self.label_send.setText(self._translate("TCP-UDP", "Send msg"))
        # self.label_dir.setText(self._translate("TCP-UDP", "请选择index.html所在的文件夹"))
        self.label_dir.setText(self._translate("TCP-UDP", "index.html 선택"))
        self.label_written.setText(self._translate("TCP-UDP", "Written by Wangler2333"))

        self.label_RD.setText(self._translate("TCP-UDP", "렌덤데이터 전송 : "))
        self.pushButton_RD_send.setText(self._translate("TCP-UDP", "Send"))

        self.label_make_csv.setText(self._translate("TCP-UDP", "csv파일만들기 :"))
        self.pushButton_make_csv.setText(self._translate("TCP-UDP", "make"))

    def connect(self):
        """
        控件信号-槽的设置
        connect 처리
        :param : QDialog类创建的对象
        :return: None
        """
        self.signal_write_msg.connect(self.write_msg)
        # currentIndexChanged : 현재 comboBox가 변경된다면 아래가 호출
        self.comboBox_tcp.currentIndexChanged.connect(self.combobox_change)

    def combobox_change(self):
        # 此函数用于选择不同功能时界面会作出相应变化
        """
        combobox控件内容改变时触发的槽
        :return: None
        """
        self.close_all()
        if self.comboBox_tcp.currentIndex() == 0 or self.comboBox_tcp.currentIndex() == 2:
            self.label_sendto.hide()
            self.label_dir.hide()
            self.pushButton_dir.hide()
            self.pushButton_send.show()
            self.lineEdit_ip_send.hide()
            self.textEdit_send.show()
            self.label_RD.hide()
            self.pushButton_RD_send.hide()
            self.label_make_csv.hide()
            self.pushButton_make_csv.hide()
            # self.label_port.setText(self._translate("TCP-UDP", "端口号:"))
            self.label_port.setText(self._translate("TCP-UDP", "Port:"))

        if self.comboBox_tcp.currentIndex() == 1 or self.comboBox_tcp.currentIndex() == 3:
            self.label_sendto.show()
            self.label_dir.hide()
            self.pushButton_dir.hide()
            self.pushButton_send.show()
            self.lineEdit_ip_send.show()
            self.textEdit_send.show()
            self.label_RD.hide()
            self.pushButton_RD_send.hide()
            self.label_make_csv.show()
            self.pushButton_make_csv.show()
            # self.label_port.setText(self._translate("TCP-UDP", "目标端口:"))
            self.label_port.setText(self._translate("TCP-UDP", "Target Port:"))

        if self.comboBox_tcp.currentIndex() == 4:
            self.label_sendto.hide()
            self.label_dir.show()
            self.pushButton_dir.show()
            self.pushButton_send.hide()
            self.lineEdit_ip_send.hide()
            self.textEdit_send.hide()
            # self.label_port.setText(self._translate("TCP-UDP", "端口号:"))
            self.label_port.setText(self._translate("TCP-UDP", "Port:"))

    def write_msg(self, msg):
        # self.signal_write_msg.emit(msg) 이런식으로 수신메시지를 보내온다.
        # signal_write_msg信号会触发这个函数
        """
        功能函数，向接收区写入数据的方法
        Receive msg를 기록한다.
        信号-槽触发
        tip：PyQt程序的子线程中，直接向主线程的界面传输字符是不符合安全原则的
        :return: None
        """
        self.textBrowser_recv.insertPlainText(msg)
        # 滚动条移动到结尾
        # 스크롤 바를 끝으로 내린다.
        self.textBrowser_recv.moveCursor(QtGui.QTextCursor.End)

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        self.close_all()

    def close_all(self):
        # pure virtual fn
        pass


if __name__ == '__main__':
    """
    显示界面
    dlg interface
    """
    app = QApplication(sys.argv)
    ui = ToolsUi(1)
    ui.show()
    sys.exit(app.exec_())

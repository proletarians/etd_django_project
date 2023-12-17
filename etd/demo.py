#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Image, Table
from reportlab.platypus import Spacer
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

pdfmetrics.registerFont(
    TTFont('STSong', r'C:\Program Files\Microsoft Office\root\vfs\Fonts\private\STSONG.TTF'))  # 替换为实际的文件路径

# 设置样式
style = getSampleStyleSheet()
normal_style = style['Normal']
normal_style.fontName = 'STSong'  # 使用注册的字体
normal_style.fontSize = 12
normal_style.leading = 20


def draw_text(st, text: str):
    return Paragraph(text, st)


def draw_img(path):
    img = Image(path)  # 读取指定路径下的图片
    img.drawWidth = 6 * cm  # 设置图片的宽度
    img.drawHeight = 5 * cm  # 设置图片的高度
    return img


def draw_table(*args):
    col_width = 120
    style = [
        ('FONTNAME', (0, 0), (-1, -1), 'song'),  # 字体
        ('FONTSIZE', (0, 0), (-1, 0), 12),  # 第一行的字体大小
        ('FONTSIZE', (0, 1), (-1, -1), 10),  # 第二行到最后一行的字体大小
        ('BACKGROUND', (0, 0), (-1, 0), '#d5dae6'),  # 设置第一行背景颜色
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 第一行水平居中
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),  # 第二行到最后一行左右左对齐
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 所有表格上下居中对齐
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.darkslategray),  # 设置表格内文字颜色
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # 设置表格框线为grey色，线宽为0.5
        ('SPAN', (0, 1), (2, 1)),  # 合并第二行一二三列
    ]
    table = Table(args, colWidths=col_width, style=style)
    return table


def draw_bar(bar_data: list, ax: list, items: list):
    drawing = Drawing(500, 200)
    bc = VerticalBarChart()
    bc.x = 45  # 整个图表的x坐标
    bc.y = 45  # 整个图表的y坐标
    bc.height = 150  # 图表的高度
    bc.width = 350  # 图表的宽度
    bc.data = bar_data
    bc.strokeColor = colors.black  # 顶部和右边轴线的颜色
    bc.valueAxis.valueMin = 0  # 设置y坐标的最小值
    bc.valueAxis.valueMax = 20  # 设置y坐标的最大值
    bc.valueAxis.valueStep = 5  # 设置y坐标的步长
    bc.categoryAxis.labels.dx = 2
    bc.categoryAxis.labels.dy = -8
    bc.categoryAxis.labels.angle = 20
    bc.categoryAxis.labels.fontName = 'song'
    bc.categoryAxis.categoryNames = ax

    # 图示
    leg = Legend()
    leg.fontName = 'song'
    leg.alignment = 'right'
    leg.boxAnchor = 'ne'
    leg.x = 475  # 图例的x坐标
    leg.y = 140
    leg.dxTextSpace = 10
    leg.columnMaximum = 3
    leg.colorNamePairs = items
    drawing.add(leg)
    drawing.add(bc)
    return drawing


from datetime import datetime


def draw_table_data():
    data = [
        ['姓名:', '张三', '编号 (ID):', 'SH003'],
        ['性别:', '女', '测试日期:', '2023/10/15'],
        ['年龄:', '48岁', '适应情况:', '适应良好'],
        ['出生日期:', '1975/10/5', '备注:', '无'],
        ['监护人:', '李四', '主测试人/签字:', '李医生'],
        ['监护人联系方式:', '13305781005', '报告日期:', datetime.now().strftime("%Y/%m/%d")]
    ]

    table = Table(data, colWidths=[4 * cm, 4 * cm, 4 * cm, 4 * cm], rowHeights=[1 * cm] * 6)

    # 添加自定义样式，这里没有添加边框样式
    style = TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, -1), 'STSong'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.darkslategray),
        ('SPAN', (1, 0), (1, -1)),  # 合并姓名列的单元格
        ('SPAN', (3, 0), (3, -1)),  # 合并编号列的单元格
        # 如果您想要确保没有边框，请确保没有GRID或BOX样式
    ])

    table.setStyle(style)
    return table


from reportlab.platypus import Table, TableStyle


def draw_line(width):
    line_style = TableStyle([
        ('LINEABOVE', (0, 0), (-1, 0), 2, colors.black),
        ('TOPPADDING', (0, 0), (-1, 0), 0),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 0),
    ])
    line_table = Table([['']], colWidths=[width], rowHeights=[0.1 * cm])
    line_table.setStyle(line_style)
    return line_table


def main(filename):
    pdfmetrics.registerFont(TTFont('song', 'STSONG.ttf'))

    style = getSampleStyleSheet()

    ts = style['Heading1']
    ts.fontName = 'song'  # 字体名
    ts.fontSize = 18  # 字体大小
    ts.leading = 30  # 行间距
    ts.alignment = 1  # 居中
    ts.bold = True

    hs = style['Heading2']
    hs.fontName = 'song'  # 字体名
    hs.fontSize = 15  # 字体大小
    hs.leading = 20  # 行间距
    hs.textColor = colors.red  # 字体颜色

    ns = style['Normal']
    ns.fontName = 'song'
    ns.fontSize = 12
    ns.wordWrap = 'CJK'  # 设置自动换行
    ns.alignment = 0  # 左对齐
    ns.firstLineIndent = 32  # 第一行开头空格
    ns.leading = 20
    image1 = draw_img(
        r'E:\微信下载\WeChat Files\wxid_umhm5t7ylkvp22\FileStorage\File\2023-12\djangoProject\documents\results\V_02.mp4_231026150833_102615232_Class.png')
    image2 = draw_img(
        r'E:\微信下载\WeChat Files\wxid_umhm5t7ylkvp22\FileStorage\File\2023-12\djangoProject\documents\results\V_02.mp4_231026150833_102615232_Regr.png')
    doc = SimpleDocTemplate(filename, pagesize=A4, topMargin=35)
    # 创建一个单行表格，每个单元格中放一个图片

    image_table_data = [[image1, image2]]
    image_table = Table(image_table_data)
    image_table_style = TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 1),  # 左边填充
        ('RIGHTPADDING', (0, 0), (-1, -1), 1),  # 右边填充
    ])
    image_table.setStyle(image_table_style)

    content = []
    content.append(draw_text(ts, '眼动测试报告单'))
    available_width = doc.width - doc.leftMargin - doc.rightMargin
    content.append(draw_line(500))
    content.append(draw_table_data())
    content.append(draw_line(500))
    content.append(image_table)

    content.append(Spacer(1, 1 * cm))
    content.append(draw_text(ns,
                             ' 《超级马里奥兄弟》于1985年9月13日发售，这是一款任天堂针对FC主机全力度身订造的游戏，被称为TV游戏奠基之作。这个游戏被赞誉为电子游戏的原始范本，确立了角色、游戏目的、流程分布、操作性、隐藏要素、BOSS、杂兵等以后通用至今的制作概念。《超级马里奥兄弟》成为游戏史首部真正意义上的超大作游戏，游戏日本本土销量总计681万份，海外累计更是达到了3342万份的天文数字。'))
    content.append(draw_text(hs, '经典游戏列表'))

    # 添加表格
    data = [
        ('经典游戏', '发布年代', '发行商'),
        ('TOP100',),
        ('超级马里奥兄弟', '1985年', '任天堂'),
        ('坦克大战', '1985年', '南梦宫'),
        ('魂斗罗', '1987年', '科乐美'),
        ('松鼠大战', '1990年', '卡普空'),
    ]
    content.append(draw_table(*data))

    # 生成图表
    content.append(draw_text(hs, '游戏厂商统计'))
    b_data = [(2, 4, 6, 12, 8, 16), (12, 14, 17, 9, 12, 7)]
    ax_data = ['任天堂', '南梦宫', '科乐美', '卡普空', '世嘉', 'SNK']
    leg_items = [(colors.red, '街机'), (colors.green, '家用机')]
    content.append(draw_bar(b_data, ax_data, leg_items))

    # 生成pdf文件
    doc = SimpleDocTemplate(filename, pagesize=A4, topMargin=35)
    doc.build(content)


if __name__ == '__main__':
    main("Replab1.pdf")



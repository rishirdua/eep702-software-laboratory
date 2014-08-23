#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QChar"
#include "cstdio"
#include "sstream"
#include "iostream"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


const char* smallNumbers[] = {
    "zero", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen"
};

QString spellHundreds(unsigned n) {
    QString res;
    if (n > 99) {
        res = smallNumbers[n/100];
        res += " hundred";
        n %= 100;
        if (n) res += " and ";
    }
    if (n >= 20) {
        static const char* Decades[] = {
            "", "", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"
        };
        res += Decades[n/10];
        n %= 10;
        if (n) res += "-";
    }
    if (n < 20 && n > 0)
        res += smallNumbers[n];
    return res;
}


const char* thousandPowers[] = {
    " billion", " million",  " thousand", "" };

typedef unsigned long Spellable;

QString spell(Spellable n) {
    if (n < 20) return smallNumbers[n];
    QString res;
    const char** pScaleName = thousandPowers;
    Spellable scaleFactor = 1000000000;	// 1 billion
    while (scaleFactor > 0) {
        if (n >= scaleFactor) {
            Spellable h = n / scaleFactor;
            res += spellHundreds(h) + *pScaleName;
            n %= scaleFactor;
            if (n) res += ", ";
        }
        scaleFactor /= 1000;
        ++pScaleName;
    }
    return res;
}


int Small(QString n) {

    if (n.compare(n, "zero")) {
        return 0;
    } else if (n.compare(n, "one")) {
        return 1;
    } else if (n.compare(n, "two")) {
        return 2;
    } else if (n.compare(n, "three")) {
        return 3;
    } else if (n.compare(n, "four")) {
        return 4;
    } else  if (n.compare(n, "five")) {
        return 5;
    } else  if (n.compare(n, "six")) {
        return 6;
    } else  if (n.compare(n, "seven")) {
        return 7;
    } else  if (n.compare(n, "eight")) {
        return 8;
    } else if (n.compare(n, "nine")) {
        return 9;
    } else  if (n.compare(n, "ten")) {
        return 10;
    } else  if (n.compare(n, "eleven")) {
        return 11;
    } else  if (n.compare(n, "twelve")) {
        return 12;
    } else  if (n.compare(n, "thirteen")) {
        return 13;
    } else  if (n.compare(n, "fourteen")) {
        return 14;
    } else  if (n.compare(n, "fifteen")) {
        return 15;
    } else  if (n.compare(n, "sixteen")) {
        return 16;
    } else  if (n.compare(n, "seventeen")) {
        return 17;
    } else  if (n.compare(n, "eighteen")) {
        return 18;
    } else  if (n.compare(n, "nineteen")) {
        return 19;
    } else  if (n.compare(n, "twenty")) {
        return 20;
    } else  if (n.compare(n, "thirty")) {
        return 30;
    } else if (n.compare(n, "forty")) {
        return 40;
    } else if (n.compare(n, "fifty")) {
        return 50;
    } else  if (n.compare(n, "sixty")) {
        return 60;
    } else  if (n.compare(n, "seventy")) {
        return 70;
    } else  if (n.compare(n, "eighty")) {
        return 80;
    } else  if (n.compare(n, "ninety")) {
        return 90;
    }

}

int Magnitude(QString n) {
    if (n.compare("thousand")) {
        return 1000;
    } else         if (n.compare("million")) {
        return 1000000;
    } else             if (n.compare("billion")) {
        return 1000000000;
    } else                 if (n.compare("trillion")) {
        return 1000000000000;
    } else                     if (n.compare("quadrillion")) {
        return 1000000000000000;
    } else                         if (n.compare("quintillion")) {
        return 1000000000000000000;
    }
}



int text2num (QString s) {
    QStringList a = s.split(" ");
    int n = 0;
    int g = 0;
    int ret = 0;
    for (int i = 0; i < a.length(); i++) {
        QString w = a.at(i);
        int x = Small(w);
        if (x!= 0) {
            g += x;
        }
        else if (w == "hundred") {
            g *= 100;
        }
        else {
            x = Magnitude(w);
        }
        if (x!= NULL) {
            n += g * x;
            g = 0;
        } else {
            ret = -100;
            return ret;
        }
        ret = n + g;

    }
}


void MainWindow::on_pushButton_clicked() {
    //MainWindow.changeEvent();
    QString number = ui->lineEdit->text();
    QString words = spell(number.toInt());
    ui->lineEdit_2->setText(words);
}

void MainWindow::on_pushButton_2_clicked()
{
    QString word = ui->lineEdit_2->text();
    int num = text2num(word);

    ui->lineEdit->setText("num");
}

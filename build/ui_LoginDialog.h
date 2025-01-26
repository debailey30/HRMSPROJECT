/********************************************************************************
** Form generated from reading UI file 'LoginDialog.ui'
**
** Created by: Qt User Interface Compiler version 6.8.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LOGINDIALOG_H
#define UI_LOGINDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_passwordlineEdit
{
public:
    QFormLayout *formLayout;
    QLabel *label;
    QLineEdit *usernamelineEdit;
    QLabel *label_2;
    QLineEdit *passwordlineEdit_2;
    QPushButton *loginButton;
    QPushButton *forgotusernameButton;

    void setupUi(QDialog *passwordlineEdit)
    {
        if (passwordlineEdit->objectName().isEmpty())
            passwordlineEdit->setObjectName("passwordlineEdit");
        passwordlineEdit->resize(400, 300);
        QFont font;
        font.setPointSize(6);
        passwordlineEdit->setFont(font);
        formLayout = new QFormLayout(passwordlineEdit);
        formLayout->setObjectName("formLayout");
        label = new QLabel(passwordlineEdit);
        label->setObjectName("label");
        QFont font1;
        font1.setFamilies({QString::fromUtf8("Lucida Calligraphy")});
        font1.setPointSize(12);
        font1.setItalic(true);
        label->setFont(font1);
        label->setFrameShape(QFrame::Shape::NoFrame);
        label->setTextFormat(Qt::TextFormat::AutoText);
        label->setScaledContents(false);

        formLayout->setWidget(0, QFormLayout::LabelRole, label);

        usernamelineEdit = new QLineEdit(passwordlineEdit);
        usernamelineEdit->setObjectName("usernamelineEdit");

        formLayout->setWidget(0, QFormLayout::FieldRole, usernamelineEdit);

        label_2 = new QLabel(passwordlineEdit);
        label_2->setObjectName("label_2");
        label_2->setFont(font1);

        formLayout->setWidget(1, QFormLayout::LabelRole, label_2);

        passwordlineEdit_2 = new QLineEdit(passwordlineEdit);
        passwordlineEdit_2->setObjectName("passwordlineEdit_2");
        passwordlineEdit_2->setEchoMode(QLineEdit::EchoMode::Password);

        formLayout->setWidget(1, QFormLayout::FieldRole, passwordlineEdit_2);

        loginButton = new QPushButton(passwordlineEdit);
        loginButton->setObjectName("loginButton");
        QFont font2;
        font2.setFamilies({QString::fromUtf8("Lucida Bright")});
        font2.setPointSize(12);
        loginButton->setFont(font2);

        formLayout->setWidget(2, QFormLayout::FieldRole, loginButton);

        forgotusernameButton = new QPushButton(passwordlineEdit);
        forgotusernameButton->setObjectName("forgotusernameButton");
        forgotusernameButton->setFlat(true);

        formLayout->setWidget(3, QFormLayout::FieldRole, forgotusernameButton);

        QWidget::setTabOrder(forgotusernameButton, usernamelineEdit);
        QWidget::setTabOrder(usernamelineEdit, passwordlineEdit_2);
        QWidget::setTabOrder(passwordlineEdit_2, loginButton);

        retranslateUi(passwordlineEdit);

        QMetaObject::connectSlotsByName(passwordlineEdit);
    } // setupUi

    void retranslateUi(QDialog *passwordlineEdit)
    {
        passwordlineEdit->setWindowTitle(QCoreApplication::translate("passwordlineEdit", "Dialog", nullptr));
        label->setText(QCoreApplication::translate("passwordlineEdit", "Username:", nullptr));
        label_2->setText(QCoreApplication::translate("passwordlineEdit", "Password:", nullptr));
        loginButton->setText(QCoreApplication::translate("passwordlineEdit", "Login", nullptr));
        forgotusernameButton->setText(QCoreApplication::translate("passwordlineEdit", "forgot username", nullptr));
    } // retranslateUi

};

namespace Ui {
    class passwordlineEdit: public Ui_passwordlineEdit {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LOGINDIALOG_H

#ifndef LOGINDIALOG_H
#define LOGINDIALOG_H

#include <QDialog>
#include "UserRoles.h"

namespace Ui {
class LoginDialog;
}

class LoginDialog : public QDialog {
    Q_OBJECT

public:
    explicit LoginDialog(QWidget *parent = nullptr);
    ~LoginDialog();
    UserRole getUserRole() const;

private slots:
    void on_loginButton_clicked();
    void on_forgotUsernameButton_clicked(); // Slot for "Forgot Username" button

private:
    Ui::LoginDialog *ui;
    UserRole userRole;
};

#endif // LOGINDIALOG_H

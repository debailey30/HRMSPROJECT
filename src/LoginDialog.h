#ifndef LOGINDIALOG_H
#define LOGINDIALOG_H

#include <QDialog>
#include "UserRoles.h"

namespace Ui {
/**
 * @class LoginDialog
 * @brief The LoginDialog class provides a dialog interface for user login.
 *
 * This class is responsible for handling the user interface and logic
 * related to user authentication. It typically includes fields for
 * entering a username and password, and buttons for submitting the
 * login information or canceling the login process.
 */
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

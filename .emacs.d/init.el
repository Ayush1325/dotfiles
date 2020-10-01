(require 'package)
(setq package-enable-at-startup nil)

(setq package-archives '(("gnu" . "https://elpa.gnu.org/packages/")
                         ("melpa" . "https://melpa.org/packages/")))

(package-initialize)

(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))

(setq byte-compile-warnings '(cl-functions))

(setq custom-file "~/.emacs.d/.emacs-custom.el")
(load custom-file)

(org-babel-load-file (expand-file-name "~/.emacs.d/config.org"))

(put 'dired-find-alternate-file 'disabled nil)
(put 'narrow-to-region 'disabled nil)

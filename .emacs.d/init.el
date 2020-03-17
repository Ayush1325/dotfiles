(require 'package)
(setq package-enable-at-startup nil)
(add-to-list 'package-archives
	     '("melpa" . "https://melpa.org/packages/")
	     '("elpa" . "https://elpa.gnu.org/packages"))
(package-initialize)

(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))

(setq custom-file "~/.emacs.d/.emacs-custom.el")
(load custom-file)

(org-babel-load-file (expand-file-name "~/.emacs.d/config.org"))

;(put 'dired-find-alternate-file 'disabled nil)

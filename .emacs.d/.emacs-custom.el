(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(aw-scope 'frame)
 '(dart-format-on-save t t)
 '(dart-sdk-path "~/flutter/bin/cache/dart-sdk/" t)
 '(dired-hide-details-hide-information-lines t)
 '(dired-listing-switches "-alh")
 '(diredp-hide-details-initially-flag t)
 '(diredp-hide-details-propagate-flag t)
 '(flutter-sdk-path "~/flutter/" t)
 '(global-dired-hide-details-mode t)
 '(global-display-line-numbers-mode t)
 '(inhabit-startup-message t)
 '(inhibit-startup-screen t)
 '(markdown-enable-math t)
 '(markdown-enable-wiki-links t)
 '(markdown-fontify-code-blocks-natively t)
 '(org-support-shift-select nil)
 '(package-selected-packages
   '(lsp-treemacs vterm clojure-snippets posframe toc-org hover yasnippet gdscript-mode rustic elfeed-goodies elfeed-protocol elfeed-org elfeed ob-rust latex-pretty-symbols auctex cider aggressive-indent smartparens rainbow-delimiters clojure-mode skewer-mode js2-mode go-mode treemacs-projectile lsp-dart yaml-mode flutter dart-mode json-mode quelpa virtualenvwrapper exec-path-from-shell aweshell system-packages auto-package-update move-text prettier-js emmet-mode web-mode company-restclient pipenv sx slime all-the-icons-ivy-rich ivy-rich hungry-delete helm-company sunrise smart-hungry-delete pdf-view-restore pdf-tools engine-mode ob-restclient restclient quelpa-use-package dired+ ibuffer-projectile adaptive-wrap vue-mode emojify company-emoji which-key use-package undo-tree try rainbow-mode paredit org-bullets org-ac multiple-cursors magit lsp-ui lsp-ivy lorem-ipsum iedit highlight-parentheses highlight-defined helm expand-region eshell-prompt-extras esh-autosuggest edit-indirect dracula-theme doom-themes doom-modeline dashboard dap-mode counsel-projectile company-lsp))
 '(server-switch-hook
   '((lambda nil
       (let
	   (server-buf)
	 (setq backup-by-copying t)))))
 '(sunrise-attributes-display-mask '(t nil nil nil nil))
 '(tool-bar-mode nil))

(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:family "JetBrainsMono Nerd Font Mono" :foundry "JB  " :slant normal :weight normal :height 179 :width normal))))
 '(aw-leading-char-face ((t (:inherit ace-jump-face-foreground :height 3.0))))
 '(markdown-header-face-1 ((t (:inherit markdown-header-face :foreground "violet red" :height 1.4))))
 '(markdown-header-face-2 ((t (:inherit markdown-header-face :foreground "medium orchid" :height 1.3))))
 '(markdown-header-face-3 ((t (:inherit markdown-header-face :foreground "chartreuse" :height 1.2))))
 '(markdown-header-face-4 ((t (:inherit markdown-header-face :foreground "orange red" :height 1.1)))))

\# Git Aliases



\## Список алиасов



| Алиас | Полная команда | Описание |

|-------|----------------|----------|

| `git st` | `git status` | Статус репозитория: изменённые файлы, staging, ветка |

| `git ci` | `git commit` | Создать коммит |

| `git co` | `git checkout` | Переключить ветку / создать / откатить файл |

| `git br` | `git branch` | Список веток, создание, удаление |

| `git df` | `git diff --stat` | Различия между рабочей папкой и staging |

| `git lg` | `git log --oneline --decorate --all --graph` | Граф всей истории |

| `git recent` | `git log --oneline -n 5` | 5 последних коммитов |

| `git undo` | `git reset --soft HEAD\~1` | Отменить последний коммит, сохранив изменения |



\## Установка



Добавьте в `\~/.gitconfig`:



```ini

\[alias]

&#x20;   st = status

&#x20;   ci = commit

&#x20;   co = checkout

&#x20;   br = branch

&#x20;   df = diff

&#x20;   lg = log --oneline --decorate --all --graph

&#x20;   recent = log --oneline -n 5

&#x20;   undo = reset --soft HEAD\~1


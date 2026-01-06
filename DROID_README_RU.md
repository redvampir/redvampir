# Droid (Factory CLI) — Быстрая инструкция (рус.)

Кратко: `droid` — CLI-агент от Factory, предоставляет интерактивный и неинтерактивный режимы для выполнения команд/запросов.

Установка и подготовка
- Положите `droid.exe` в `%USERPROFILE%\bin` и убедитесь, что эта папка в PATH (или используйте явный путь).
- При необходимости разблокируйте файл: `Unblock-File "$env:USERPROFILE\bin\droid.exe"`.
- Перезапустите VS Code/терминал или настройте локальный PATH в `.vscode/settings.json`.

Основные опции
- `-v, --version` — показать версию (пример: `droid --version`).
- `-h, --help` — показать справку.
- `-r, --resume [sessionId]` — возобновить сессию (по умолчанию — последняя).

Режимы и команды
- Интерактивный режим (по умолчанию): просто выполните `droid` — откроется REPL-подобный режим.
- Одноразовый/non-interactive: `droid exec "текст запроса"` — выполнит команду и выйдет.
  - Можно читать из stdin: `droid exec - < prompt.txt`.
- Команды:
  - `exec` — выполнить единичный запрос (см. выше).
  - `mcp` — управление MCP серверами (см. `droid mcp --help` для опций).

Примеры использования
- Быстрый интерактивный старт:
  ```powershell
  droid
  ```
- Запуск с начальным запросом (интерактивно):
  ```powershell
  droid "review src/index.tsx"
  ```
- Скриптовый/неинтерактивный запуск:
  ```powershell
  droid exec "analyze this file"
  droid exec - < changes_prompt.txt
  ```
- Помощь по конкретной команде:
  ```powershell
  droid exec --help
  droid mcp --help
  ```

Интеграция с VS Code
- Добавленная задача: [.vscode/tasks.json](.vscode/tasks.json) (запускает `droid --version` и `droid --help` по явному пути `${env:USERPROFILE}\bin\droid.exe`).
- Откройте Command Palette → Run Task → выберите задачу.
- Для запуска в терминале: откройте новый терминал в VS Code и выполните `droid ...`.

Диагностика
- Если команда не найдена: проверьте, что `%USERPROFILE%\bin` в PATH, либо запустите явно:
  ```powershell
  & "$env:USERPROFILE\bin\droid.exe" --version
  ```
- Если Windows блокирует файл: `Unblock-File 'путь\droid.exe'`.
- Проверить SHA256: `Get-FileHash 'путь\droid.exe' -Algorithm SHA256`.

Где смотреть документацию
- Официальное руководство: https://docs.factory.ai/factory-cli/getting-started/overview

---
Файл сгенерирован автоматически — скажите, если нужно расширить секции (логин/инициализация/DEPLOY примеры) или перевести дополнительные опции в подробный справочник.

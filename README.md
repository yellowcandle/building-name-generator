# 唐樓命名攻略

這是一個使用 Streamlit 構建的應用程序，用於生成傳統唐樓名稱。

## 原 post

https://www.threads.net/@hkcornerhouses/post/DASXHABSXVa

## 功能

- 選擇字頭類別：時間、地方、數量、意頭和其他
- 隨機生成大廈名稱
- 顯示生成的大廈名稱和使用的字頭類別
- 提供命名策略說明
- 顯示參考圖片

## 線上版本

GitHub Pages（靜態版，毋須安裝即可使用）：
https://yellowcandle.github.io/building-name-generator/

## 使用方法

### 線上（GitHub Pages）

直接打開上方連結即可使用，毋須任何安裝。

### 本地開發（Streamlit）

1. Clone 此 repo。
2. 確保已安裝 Streamlit 和其他必要的依賴項（`uv sync`）。
3. 在命令行中運行 `uv run streamlit run app.py`。
4. 在瀏覽器中打開生成的本地地址以訪問應用程序。

## 部署（GitHub Pages）

`index.html` 是一個自足的靜態頁面（內嵌字型、純前端邏輯），可直接由 GitHub Pages 提供。
一次性設定：**Settings → Pages → Build and deployment → Deploy from a branch →
分支 `main`、資料夾 `/ (root)`**。推送到 `main` 後數分鐘即會上線。

`.nojekyll` 確保 Pages 原樣提供檔案（不經 Jekyll 處理）。

## 代碼結構

- `index.html`：部署到 GitHub Pages 的靜態單頁版本（純 HTML/CSS/JS，內嵌字型）。
- `app.py`：本地 Streamlit 版本，包含所有功能和界面設置。

## 截圖

![應用程序截圖](461008388_1761486387931403_1695198223138866317_n.jpg)

## 聲明

圖片來源: HKU Digital Repository 「聯和大廈」售樓書

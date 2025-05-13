# PowerShell スクリプト（deploy.ps1）

# プロジェクトID、アプリ名、リージョンを設定
$PROJECT_ID = "python-op-373206"
$APP_NAME = "my-app"
$REGION = "asia-northeast1"


# Cloud Run にデプロイ
gcloud run deploy $APP_NAME `
  --source . `
  --platform managed `
  --region $REGION `
  --project $PROJECT_ID `
  --allow-unauthenticated

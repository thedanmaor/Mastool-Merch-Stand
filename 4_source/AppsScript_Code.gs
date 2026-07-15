/**
 * MasTool VIP Signup — Apps Script Web App
 *
 * Setup:
 * 1. Create a Google Sheet named "MasTool VIP Signups" in Drive.
 * 2. Extensions > Apps Script. Delete the default code, paste this file's contents.
 * 3. Deploy > New deployment > type "Web app".
 *    Execute as: Me. Who has access: Anyone.
 * 4. Click Deploy, authorize when prompted, copy the Web app URL.
 * 5. Send that URL back — it gets pasted into FORM_ENDPOINT in vip.html.
 */
function doPost(e) {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Signups')
             || SpreadsheetApp.getActiveSpreadsheet().insertSheet('Signups');

  if (sheet.getLastRow() === 0) {
    sheet.appendRow(['Timestamp', 'Name', 'Phone', 'Email', 'Consent', 'Source', 'Show']);
  }

  const data = JSON.parse(e.postData.contents);
  sheet.appendRow([
    new Date(),
    data.name || '',
    data.phone || '',
    data.email || '',
    data.consent === true,
    data.source || '',
    data.show || ''
  ]);

  return ContentService
    .createTextOutput(JSON.stringify({ ok: true }))
    .setMimeType(ContentService.MimeType.JSON);
}

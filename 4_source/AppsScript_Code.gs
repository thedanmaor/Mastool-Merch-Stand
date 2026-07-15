/**
 * MasTool VIP Signup — Apps Script Web App
 *
 * Target sheet: https://docs.google.com/spreadsheets/d/1x1tHs_A7NkoUK5WYNbNCQLI_RxWpS0_iRt7_m3_r2Ic/edit
 *
 * Setup:
 * 1. Open the sheet above. Extensions > Apps Script. Delete the default code, paste this file's contents.
 * 2. Deploy > New deployment > type "Web app".
 *    Execute as: Me. Who has access: Anyone.
 * 3. Click Deploy, authorize when prompted, copy the Web app URL.
 * 4. Send that URL back — it gets pasted into FORM_ENDPOINT in vip.html.
 */
const SHEET_ID = '1x1tHs_A7NkoUK5WYNbNCQLI_RxWpS0_iRt7_m3_r2Ic';

function doPost(e) {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  const sheet = ss.getSheetByName('Signups') || ss.insertSheet('Signups');

  if (sheet.getLastRow() === 0) {
    sheet.appendRow(['Timestamp', 'Name', 'Phone', 'Email', 'Consent', 'Shirt', 'Shirt Size', 'Event Poster', 'Ltd Poster', 'Source', 'Show']);
  }

  const data = JSON.parse(e.postData.contents);
  sheet.appendRow([
    new Date(),
    data.name || '',
    data.phone || '',
    data.email || '',
    data.consent === true,
    data.shirt === true,
    data.shirtSize || '',
    data.eventPoster === true,
    data.ltdPoster === true,
    data.source || '',
    data.show || ''
  ]);

  return ContentService
    .createTextOutput(JSON.stringify({ ok: true }))
    .setMimeType(ContentService.MimeType.JSON);
}

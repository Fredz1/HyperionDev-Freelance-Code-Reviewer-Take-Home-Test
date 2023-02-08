var caesarCipher = function (string, shift) {
    var alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    var encodedText = '';
    if (shift > 26) {
        shift = shift % 26;
    }
    var i = 0;
    while (i < string.length) {
        if (alphabet.indexOf(string[i]) !== -1) {
            var alphabetIndex = alphabet.indexOf((string[i]).toUpperCase());
            if (alphabet[alphabetIndex + shift]) {
                encodedText += alphabet[alphabetIndex + shift];
            }
            else {
                encodedText += alphabet[alphabetIndex + shift - 26];
            }
        }
        else {
            encodedText += string[i];
        }
        i++;
    }
    return encodedText;
};
console.log(caesarCipher('GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.', 39));

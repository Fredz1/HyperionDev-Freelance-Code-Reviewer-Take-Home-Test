type Alphabetype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

const caesarCipher = (string: string, shift: number) => {
  const alphabet: Alphabetype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

  let encodedText: string = '';

  if (shift > 26) {
    shift = shift % 26;
  }

  let i: number = 0;
  while (i < string.length) {
    if (alphabet.indexOf(string[i]) !== -1) {
      const alphabetIndex: number = alphabet.indexOf((string[i]).toUpperCase());

      if (alphabet[alphabetIndex + shift]) {
        encodedText += alphabet[alphabetIndex + shift];
      } else {
        encodedText += alphabet[alphabetIndex + shift - 26];
      }
    } else {
      encodedText += string[i];
    }

    i++;
  }

  return encodedText;
};

console.log(caesar_cipher('GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.', 39));
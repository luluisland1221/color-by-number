# Development Guidelines for color-by-number.site

## Language Policy
**STRICTLY ENGLISH ONLY** - This website is designed for English-speaking users. All user-facing content must be in English.

### Forbidden Elements:
- Chinese characters (CJK Unified Ideographs)
- Chinese punctuation marks （）
- Chinese numbers (一, 二, 三, etc.)
- Chinese technical terms
- Any other non-English text in user-facing content

### Required Elements:
- All HTML lang attributes must be `lang="en"`
- All page titles must be in English
- All meta descriptions must be in English
- All navigation text must be in English
- All button text must be in English
- All footer text must be in English

## File Structure
- Use English filenames only
- Use English folder names only
- Avoid special characters in filenames
- Use hyphens instead of spaces in URLs

## Code Comments
- Development tools and scripts may use Chinese comments for internal use
- All user-facing content must remain in English
- Avoid Chinese comments in HTML, CSS, and JavaScript files that users might see

## Verification Checklist
Before committing changes, verify:
- [ ] No Chinese characters in any HTML content
- [ ] No Chinese characters in page titles
- [ ] No Chinese characters in meta descriptions
- [ ] All navigation text is in English
- [ ] All button labels are in English
- [ ] All footer content is in English
- [ ] All PDF filenames referenced are in English
- [ ] All return links point to correct English pages

## Error Prevention
- Use regex search for Chinese characters: `[\u4e00-\u9fff]`
- Check file encoding (should be UTF-8)
- Verify all href attributes point to English filenames
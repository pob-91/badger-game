using UnityEngine;

public class RepeatingBackgroundController : MonoBehaviour
{
    #region Private

    private BoxCollider2D _bx2d;
    private float _groundHorizontalLength;

    #endregion

    #region Loop

    // Use this for initialization
    void Start()
    {
        _bx2d = GetComponent<BoxCollider2D>();
        _groundHorizontalLength = _bx2d.size.x;
    }

    // Update is called once per frame
    void Update()
    {
        if (transform.position.x < -_groundHorizontalLength)
        {
            RepositionBackground();
        }
    }

    #endregion

    #region Private

    private void RepositionBackground()
    {
        var groundOffset = new Vector2(_groundHorizontalLength * 2, 0);
        transform.position = (Vector2)transform.position + groundOffset;
    }

    #endregion
}

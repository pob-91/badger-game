using UnityEngine;

public class ScrollingObjectController : MonoBehaviour
{
    #region Public

    #endregion

    #region Private

    private Rigidbody2D _rb2d;

    #endregion

    #region Loop

    // Use this for initialization
    void Start()
    {
        _rb2d = GetComponent<Rigidbody2D>();
        _rb2d.velocity = new Vector2(GameController.Instance.ScrollSpeed, 0);
    }

    // Update is called once per frame
    void Update()
    {
        if (GameController.Instance.GameOver)
        {
            _rb2d.velocity = Vector2.zero;
        }
    }

    #endregion
}

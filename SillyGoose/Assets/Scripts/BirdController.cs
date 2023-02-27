using UnityEngine;

public class BirdController : MonoBehaviour
{
    #region Public

    public float UpForce = 200f;

    #endregion

    #region Private

    private bool _isDead;
    private Rigidbody2D _rb2d;
    private Animator _anim;

    #endregion

    #region Loop

    // Use this for initialization
    void Start()
    {
        _rb2d = GetComponent<Rigidbody2D>();
        _anim = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        if (_isDead) return;

        if (Input.GetMouseButtonDown(0))
        {
            _rb2d.velocity = Vector2.zero;
            _rb2d.AddForce(new Vector2(0, UpForce));
            _anim.SetTrigger("Flap");
        }
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        _rb2d.velocity = Vector2.zero;
        _isDead = true;
        _anim.SetTrigger("Die");
        GameController.Instance.BirdDied();
    }

    #endregion
}
